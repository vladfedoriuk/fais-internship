# The first instruction is what image we want to base our container on
FROM python:3.9.1

RUN adduser --disabled-password --gecos '' praktyki

# The environment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# development
ENV DEBUG 1

# environment variables to ensure the database access
ENV MYSQL_DATABASE: praktyki
ENV MYSQL_USER: praktyki
ENV MYSQL_PASSWORD: pass4praktyki
ENV MYSQL_HOST database
ENV MYSQL_PORT 3306

# create root directory for our project in the container
RUN mkdir /code

# Copy the current directory contents into the container at /code
COPY . /code
RUN chown -R praktyki /code

# Copy the entrypoint and grant the user required rights.
COPY ./compose/app/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN chown praktyki /entrypoint.sh

USER praktyki
# Set the working directory to /code
WORKDIR /code

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["/entrypoint.sh"]
