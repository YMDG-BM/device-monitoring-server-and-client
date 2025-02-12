# 使用官方的 Python 基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录的内容到工作目录
COPY . /app

# 安装依赖项
RUN pip install --no-cache-dir -r requirements.txt

# 暴露 Flask 应用运行的端口
EXPOSE 5000

# 设置环境变量
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0

# 运行 Flask 应用