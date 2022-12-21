# syntax=docker/dockerfile:1
FROM python:3.9.14-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt 
COPY honk.py honk.py
ENV api_token=API_TOKEN
CMD [ "python3", "./honk.py"]