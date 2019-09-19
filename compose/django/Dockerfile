FROM python:3.6-alpine
RUN apk add build-base
RUN apk add --no-cache jpeg-dev zlib-dev
WORKDIR /app/
COPY ./backend/requirements.txt .
RUN python3 -m pip install -r requirements.txt --no-cache-dir
RUN addgroup -S django && adduser -S django -G django
COPY backend/ .
RUN chown -R django /app
RUN python3 manage.py migrate
COPY ./compose/django/gunicorn.sh /gunicorn.sh
RUN sed -i 's/\r//' /gunicorn.sh \
    && chmod +x /gunicorn.sh \
    && chown django /gunicorn.sh
RUN exec "$0"