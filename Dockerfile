# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the calculator package and tests
COPY calculator/ /app/calculator/
COPY tests/ /app/tests/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point
CMD ["python", "-m", "calculator.main"] 