# Usar uma imagem base do Python
FROM python:3.11

# Instalar librabbitmq-dev e outras dependências
RUN apt-get update && apt-get install -y \
    librabbitmq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /app

ENV PYTHONPATH="${PYTHONPATH}:/app"

# Copiar o código fonte para a imagem
COPY . .

# Copiar os arquivos de requisitos
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt


# Expor a porta em que o FastAPI estará rodando
EXPOSE 8000

# Comando para iniciar o servidor FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
