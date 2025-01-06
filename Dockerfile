# Use a lightweight Python base image
FROM python:3.11-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the OS dependencies file to the container
COPY apt-packages.txt .

# Install necessary packages from the dependencies file
RUN apt-get update && xargs -a apt-packages.txt apt-get install -y && apt-get clean

# Copy application files and requirements.txt to the container
COPY . .

# Create a virtual environment
RUN python -m venv venv

# Install Python dependencies in the virtual environment
RUN ./venv/bin/pip install --no-cache-dir -r requirements.txt

# Set the environment variable for the virtual environment
ENV PATH="/app/venv/bin:$PATH"

# Command to run the bot
CMD ["python", "main.py"]
