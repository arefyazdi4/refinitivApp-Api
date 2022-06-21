FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN addgroup app && adduser -S -G app app
USER app

# RUN apt-get install python3-dev python3-pip gcc -y
RUN apk update && apk add python3-dev

# Change work directory
WORKDIR /app

# Install application dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --upgrade pip

# Copy the application files into the image
COPY . .

# Expose port 8000 on the container
EXPOSE 8000

# Define an Entrypoint
CMD ["python", "manage.py", "runserver"]