# Use a base image with a Python runtime
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set the entry point command to run app.py
CMD ["streamlit", "run", "app.py"]
