FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# RUN apt-get install python3-dev python3-pip gcc -y
RUN apk update && apk add python3-dev
RUN apk add g++ gcc musl-dev libffi-dev openssl-dev

# Change work directory
WORKDIR /app

# Install application dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

# Copy the application files into the image
COPY . .

# Expose port 8000 on the container
EXPOSE 8000

# Crating user with limited lavrage to preventing any possible penetration
RUN addgroup -S app && adduser -S -G app app
USER app

# Define an Entrypoint
CMD ["python", "manage.py", "runserver"]
