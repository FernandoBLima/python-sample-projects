FROM python:3.8

# Make a directory for our app
WORKDIR /api

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy our source code
COPY . .

# Run the application
CMD ["python", "app.py"]