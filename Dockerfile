# Use an official lightweight Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your Python file into the container
COPY demo.py .

# Run the script when the container starts
CMD ["python", "demo.py"]
