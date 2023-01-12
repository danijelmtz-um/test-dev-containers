FROM python:3.9
RUN apt update && apt install -y sudo

## Pip dependencies 
RUN pip install --upgrade pip 
COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt
