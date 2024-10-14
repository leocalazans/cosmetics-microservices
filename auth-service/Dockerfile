FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# RUN pip install uvicorn

# RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN pip install fastapi uvicorn

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
