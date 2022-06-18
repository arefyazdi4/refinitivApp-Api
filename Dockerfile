FROM python:3.9-alpine
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
RUN pip install --upgrade pip
EXPOSE 8000
