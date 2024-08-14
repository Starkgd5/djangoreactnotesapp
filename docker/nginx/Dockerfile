# Use a imagem oficial do Nginx baseada no Alpine
FROM nginx:stable-alpine

# Remova a configuração padrão do Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copie a configuração personalizada do Nginx para o diretório de configuração
COPY ./docker/nginx/nginx.conf /etc/nginx/conf.d/nginx.conf

# Use o comando de depuração do Nginx para manter o daemon em execução em primeiro plano
CMD ["nginx-debug", "-g", "daemon off;"]
