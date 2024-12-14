#!/bin/bash

# 定义日志文件所在目录，如果不存在则创建
LOG_DIR="$HOME/beb_logs"
mkdir -p "$LOG_DIR"

# 获取当前日期，格式为 YYYYmmdd，用于日志文件名
timestamp=$(date +%Y%m%d)

# 检查环境变量 BEB_MODEL_PATH 是否设置，如果未设置则报错并退出脚本
if [ -z "$BEB_MODEL_PATH" ]; then
    echo "Error: BEB_MODEL_PATH environment variable is not set."
    exit 1
fi

# 构建完整的日志文件路径
log_file="${LOG_DIR}/${timestamp}.log"

# 启动vllm的api_server进程，并将输出重定向到日志文件，后台运行
nohup python -m vllm.entrypoints.openai.api_server \
    --model "$BEB_MODEL_PATH" \
    --served-model-name "beb" \
    --api-key beb \
    --trust-remote-code \
    >> "$log_file" 2>&1 &

# 获取刚启动进程的PID，以便后续可能的管理或监控等操作（比如可以记录下来后续查看进程状态等）
pid=$!
echo "vllm.api_server process started with PID: $pid. Logging to $log_file"