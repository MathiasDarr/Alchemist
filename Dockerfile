FROM python:3.8-slim
RUN apt-get -y update && apt-get install -y curl gnupg

WORKDIR /app

COPY application application
COPY wsgi.py wsgi.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# ADD . .
# RUN pip install .

CMD gunicorn --workers 2 --timeout 1200 --bind 0.0.0.0:8080 --access-logfile - wsgi:application --reload