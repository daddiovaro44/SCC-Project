FROM python:3.10.9-slim-buster
WORKDIR /pipeline
COPY requirements_dd.txt /pipeline
RUN pip install -r requirements_dd.txt
COPY download_data.py /pipeline
