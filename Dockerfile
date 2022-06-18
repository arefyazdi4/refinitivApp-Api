FROM python:3.9-alpine
ENV PYTHONUNBUFFERED=1

RUN addgroup app && adduser -S -G app app
USER app
RUN apk update && apk add python3-dev

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
RUN pip install --upgrade pip
EXPOSE 8000
