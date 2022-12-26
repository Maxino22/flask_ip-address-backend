FROM python:3.8-slim

# Create a working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app code
COPY app.py .

# # Specify the command to run when the container starts
# CMD ["flask", "run", "--host=0.0.0.0"]

# Start the app with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]