# syntax=docker/dockerfile:1
FROM python:3
WORKDIR /app
COPY requirements.txt requirements.txt
RUN python3 -m pip install --no-cache-dir -r requirements.txt 
COPY honk.py honk.py
ENV api_token=""
CMD [ "python3", "./honk.py"]