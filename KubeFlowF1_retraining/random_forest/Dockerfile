FROM python:3.10.9-slim-buster
WORKDIR /pipeline
COPY requirements_rf.txt /pipeline
RUN pip install -r requirements_rf.txt
COPY random_forest_retraining.py /pipeline
COPY random_forest.joblib /pipeline
