# Use the Python 3.8 slim-buster base image
FROM python:3.8-slim-buster

# Copy the contents of the local "app" directory to the /app directory in the Docker image
COPY . /app

# Set the working directory inside the container to /app
WORKDIR /app 

# Update package lists and install the AWS CLI
RUN apt update -y && apt install awscli -y 

# Install Python dependencies listed in the requirements.txt file
RUN pip install -r requirements.txt 

# Set the default command to run when the container starts
CMD ["python3", "app.py"]