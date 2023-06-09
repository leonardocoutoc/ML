FROM python:alpine3.17
WORKDIR /opt/ml_app/
RUN apk add git mysql-client mariadb-connector-c && git clone https://github.com/leonardocoutoc/ML
RUN python3 -m venv ML
RUN pip install mysql-connector-python
