#!/bin/bash
# 定义要查找和杀死的进程关键字
process_keyword="python -m vllm"
# 使用pgrep命令查找进程的PID（进程标识符）
pids=$(pgrep -f $process_keyword)
if [ -n "$pids" ]; then
  # 如果找到进程，循环遍历每个PID并杀死进程
  for pid in $pids; do
    echo "正在杀死进程 $pid"
    kill -9 $pid
  done
else
  echo "未找到包含关键字 $process_keyword 的进程。"
end