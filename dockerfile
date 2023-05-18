FROM python:3.10

# 设置工作目录
WORKDIR /code

# 复制源代码到工作目录
COPY . .

# 安装依赖项
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
# RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 暴露端口
EXPOSE 8885

# 启动Flask应用程序
CMD ["python3", "app.py"]
