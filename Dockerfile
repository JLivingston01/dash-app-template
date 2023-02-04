FROM python:3.11-slim-buster
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
#ENTRYPOINT [ "flask","--app","app/app","run","--host=0.0.0.0","--port=8050" ]
ENTRYPOINT [ "gunicorn -w 2 -b 0.0.0.0:5000 wsgi:app"]