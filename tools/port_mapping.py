import pexpect
import os

# 获取特定环境变量的值
# 与vllm部署的网络参数一致
# 配置参数


def port_mapping():
    port = os.environ.get("BEB_PORT")
    url = os.environ.get("BEB_URL")
    password = os.environ.get("BEB_PASSWORD")
    command = f"ssh -CNg -L 8000:127.0.0.1:8000 root@{url} -p {port} -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"
    # 启动 ssh 连接
    try:
        child = pexpect.spawn(command)

        # 等待密码提示
        child.expect("password:")

        # 输入密码
        child.sendline(password)
        print("success")
        # 保持连接
        # child.interact()

    except pexpect.exceptions.EOF:
        print("连接失败，检查命令或服务器状态！")
    except pexpect.exceptions.TIMEOUT:
        print("连接超时，请检查网络或服务器端口！")
