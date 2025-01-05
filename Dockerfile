# Use a lightweight Python base image
FROM python:3.11-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Install necessary packages
RUN apt-get update && apt-get install -y git && apt-get clean

# Clone the public repository directly into the working directory
RUN git clone https://github.com/Allie-Leth/ariane-bot.git .  # Use '.' instead of '/app'

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the bot
CMD ["python", "main.py"]
