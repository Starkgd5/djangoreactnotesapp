# Use uma imagem base oficial do Python
FROM python:3.11.9-slim

# Defina variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

# Defina o diretório de trabalho
WORKDIR /

# Instale dependências de sistema necessárias
RUN apt-get update && \
    apt-get install -y netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

# Copie os arquivos da aplicação para o contêiner
COPY . .

# Instale as dependências do Python
RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -r requirements.txt && \
    chmod +x ./entrypoint.sh

# Defina o comando de entrada
CMD ["./entrypoint.sh"]
