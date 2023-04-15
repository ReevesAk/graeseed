# Start from the official Python base image.
FROM python:3.9

# Set the current working directory to /code.
WORKDIR /code

# Copy the file with the requirements to the /code directory.
COPY ./requirements.txt /code/requirements.txt

# Install the package dependencies in the requirements file.
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt 

# Install other package dependencies.
RUN pip install tortoise-orm && pip install tortoise-orm[asyncpg] && pip install pytest

# Copy the ./ directory inside the /code directory.
COPY ./ /code/app
