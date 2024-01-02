FROM python:3.10.9-slim-buster
WORKDIR /pipeline
COPY requirements_ld.txt /pipeline
RUN pip install -r requirements_ld.txt
COPY load_data_retraining.py /pipeline
COPY F1_retraining.csv /pipeline
