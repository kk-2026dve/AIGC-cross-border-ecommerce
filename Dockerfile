# 使用官方 Python 基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制依赖清单并安装（使用了清华源加速）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 复制所有代码到容器里
COPY . .

# 启动命令（已修改为你实际的文件名 run.py）
CMD ["python", "run.py"]