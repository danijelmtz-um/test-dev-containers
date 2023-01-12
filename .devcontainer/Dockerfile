# Use Python 3.9 as the base image
FROM python:3.9

# Update package manager and install sudo
RUN apt update && apt install -y sudo

# Upgrade pip
RUN pip install --upgrade pip 

# Copy requirements.txt to the /tmp directory
COPY requirements.txt /tmp/requirements.txt

# Install dependencies from requirements.txt
RUN pip install -r /tmp/requirements.txt
