# Set Up Base Image
FROM python:3
LABEL maintainer="Christian Andersen <c.andersen2012@gmail.com>"

# Install Dependencies
COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the App to the container
COPY . /app

# Run the app
ENTRYPOINT [ "python" ]
CMD ["main.py"]