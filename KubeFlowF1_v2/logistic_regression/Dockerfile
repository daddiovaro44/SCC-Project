FROM python:3.10.9-slim-buster
WORKDIR /pipeline
COPY requirements_lr.txt /pipeline
RUN pip install -r requirements_lr.txt
COPY logistic_regression.py /pipeline
