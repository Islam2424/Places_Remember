# Dockerfile
FROM python:3.9-buster

# Установка nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# копирование и установка dependencies
RUN mkdir -p /PycharmProjects/Places_Remember
RUN mkdir -p /PycharmProjects/Places_Remember/pip_cache
RUN mkdir -p /PycharmProjects/Places_Remember/Places_Remember
COPY requirements.txt start-server.sh /PycharmProjects/Places_Remember/
COPY .pip_cache /PycharmProjects/Places_Remember/pip_cache/
COPY Places_Remember /PycharmProjects/Places_Remember/
WORKDIR /PycharmProjects/Places_Remember
RUN pip install -r requirements.txt --cache-dir /PycharmProjects/Places_Remember/pip_cache
RUN chown -R www-data:www-data /PycharmProjects/Places_Remember

# Запуск сервера
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/PycharmProjects/Places_Remember/start-server.sh"]

