# Which image of Python get from docker hub
FROM python:3.10.9-slim-buster

# Working directory in the container where source code and others files will be located
WORKDIR /app

# Copy requirements and run installations
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

# Expose port
EXPOSE 8501

# Copy all files from local directory to container directory
COPY . /app

# Create an entry point to make the image executable
ENTRYPOINT ["streamlit", "run"]

# Run the application
CMD ["web_app.py"]



