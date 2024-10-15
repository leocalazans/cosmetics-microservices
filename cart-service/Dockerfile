FROM python:3.9-slim

RUN apt-get update && apt-get install -y wget && \
    wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz && \
    tar -C /usr/local/bin -xzf dockerize-linux-amd64-v0.6.1.tar.gz && \
    rm dockerize-linux-amd64-v0.6.1.tar.gz

WORKDIR /app

COPY requirements.txt .

COPY . /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN pip install fastapi uvicorn

CMD ["dockerize", "-wait", "tcp://postgres:5432", "-timeout", "30s", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
