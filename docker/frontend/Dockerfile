# Use uma imagem base oficial do Node.js baseada no Alpine
FROM node:alpine

# Defina o diretório de trabalho
WORKDIR /frontend

# Instale dependências de sistema necessárias
RUN apk update && \
    apk add --no-cache netcat-openbsd

# Copie os arquivos da aplicação para o contêiner
COPY ./frontend .

# Instale as dependências do projeto
RUN npm install

# Instale o serve globalmente
RUN npm install -g serve

# Comando de entrada para iniciar a aplicação
CMD [ "serve", "-s", "build" ]
