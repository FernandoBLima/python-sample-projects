FROM python:3.8

# Make a directory for our app
WORKDIR /server

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy our source code
COPY ./api .
ENV HOME=SERVER

# Run the application
CMD ["python", "index.py"]