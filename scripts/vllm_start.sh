set -e

HOST_ADDR=0.0.0.0
CONTROLER_PORT=28777
WORKER_BASE_PORT=11160

PYTHON_EXECUTABLE=$(which python3)

MODEL_BASE=/root/finetune/work_dirs/assistTuner/
CUDA_DEVICE_BASE=0
POLICY_MODEL_NAME=beb

MODEL_PATH=$MODEL_BASE/$POLICY_MODEL_NAME


LOGDIR=logs_fastchat

tmux start-server
tmux new-session -s FastChat1 -n controller -d
tmux send-keys "export LOGDIR=${LOGDIR}" Enter
tmux send-keys "$PYTHON_EXECUTABLE -m fastchat.serve.controller --port ${CONTROLER_PORT} --host $HOST_ADDR" Enter


echo "Wait 10 seconds ..."
sleep 5

echo "Starting workers"

WORKER_PORT=$((WORKER_BASE_PORT))
tmux new-window -n policy_worker
tmux send-keys "export LOGDIR=${LOGDIR}" Enter
tmux send-keys "CUDA_VISIBLE_DEVICES=$((i+CUDA_DEVICE_BASE)) $PYTHON_EXECUTABLE -m reason.llm_service.workers.vllm_worker --model-path $MODEL_PATH --controller-address http://$HOST_ADDR:$CONTROLER_PORT --host $HOST_ADDR --port $WORKER_PORT --worker-address http://$HOST_ADDR:$WORKER_PORT --dtype bfloat16 --swap-space 32" Enter

