"""This script refers to the dialogue example of streamlit, the interactive
generation code of chatglm2 and transformers.

We mainly modified part of the code logic to adapt to the
generation of our model.
Please refer to these links below for more information:
    1. streamlit chat example:
        https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps
    2. chatglm2:
        https://github.com/THUDM/ChatGLM2-6B
    3. transformers:
        https://github.com/huggingface/transformers
Please run with the command `streamlit run path/to/web_demo.py
    --server.address=0.0.0.0 --server.port 7860`.
Using `python path/to/web_demo.py` may cause unknown problems.

"""

# import openai
import streamlit as st
from openai import OpenAI
import tools.port_mapping
import base64

from dataclasses import asdict, dataclass


# Set OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "beb"
openai_api_base = "http://localhost:8000/v1"
model_name = "beb"
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)


@dataclass
class GenerationConfig:
    # this config is used for chat to provide more diversity
    max_length: int = 32768
    top_p: float = 1.0
    temperature: float = 0.7


def prepare_generation_config():
    with st.sidebar:
        max_length = st.slider("Max Length", min_value=8, max_value=32768, value=32768)
        top_p = st.slider("Top P", 0.0, 1.0, 1.0, step=0.01)
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7, step=0.01)
        st.button("Clear Chat History", on_click=on_btn_click)

    generation_config = GenerationConfig(max_length=max_length, top_p=top_p, temperature=temperature)

    return generation_config


def set_background_image(image_file):
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    page_bg_img = f"""
    <style>
    body {{
        background-image: url("data:image/jpeg;base64,{b64_encoded}");
        background-size: cover;
        background - position: center center;
        background - attachment: fixed;
        opacity: 0.5;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)


# 新的 generate_interactive 函数，使用 OpenAI API
def generate_openai_response(prompt, config):
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        stream=True,
        max_tokens=config.max_length,
        temperature=config.temperature,
        top_p=config.top_p,
    )
    return response


def on_btn_click():
    del st.session_state.messages


user_prompt = "<|im_start|>user\n{user}<|im_end|>\n"
robot_prompt = "<|im_start|>assistant\n{robot}<|im_end|>\n"
cur_query_prompt = "<|im_start|>user\n{user}<|im_end|>\n\
    <|im_start|>assistant\n"


def combine_history(prompt):
    messages = st.session_state.messages
    meta_instruction = "You are a helpful, honest, " "and harmless AI assistant."
    total_prompt = f"<s><|im_start|>system\n{meta_instruction}<|im_end|>\n"
    for message in messages:
        cur_content = message["content"]
        if message["role"] == "user":
            cur_prompt = user_prompt.format(user=cur_content)
        elif message["role"] == "robot":
            cur_prompt = robot_prompt.format(robot=cur_content)
        else:
            raise RuntimeError
        total_prompt += cur_prompt
    total_prompt = total_prompt + cur_query_prompt.format(user=prompt)
    return total_prompt


def main():
    # set_background_image("./static/pic/封面.jpeg")
    st.title("BEAUTIFY EVERY BEAUTY")

    print("START!")
    generation_config = prepare_generation_config()

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=message.get("avatar")):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("您今天更加美丽了~"):
        # Display user message in chat message container

        with st.chat_message("user", avatar="user"):

            st.markdown(prompt)
        real_prompt = combine_history(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt, "avatar": "user"})

        with st.chat_message("robot", avatar="assistant"):

            message_placeholder = st.empty()
            response_stream = generate_openai_response(real_prompt, generation_config)

            cur_text = ""
            for cur_response in response_stream:

                cur_text += cur_response.choices[0].delta.content
                message_placeholder.markdown(cur_text + "▌")

            message_placeholder.markdown(cur_text)
            # st.markdown(response)
            # Add robot response to chat history
            st.session_state.messages.append(
                {
                    "role": "robot",
                    "content": cur_text,  # pylint: disable=undefined-loop-variable
                    "avatar": "assistant",
                }
            )


if __name__ == "__main__":
    main()
