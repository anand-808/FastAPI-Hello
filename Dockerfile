# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the app will run on
EXPOSE 8000

# Command to run the FastAPI app with Uvicorn, specifying the app module
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
