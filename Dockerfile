FROM python:3.8-alpine
RUN apk update && apk add --no-cache python3-dev gcc libc-dev
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .