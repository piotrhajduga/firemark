# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8

# Allows docker to cache installed dependencies between builds
COPY firemark_django/requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY firemark_django application
WORKDIR /application

EXPOSE 8000

ENV FIREMARK_SQLITE_DIR "/firemark_sqlite"


# runs the production server
ENTRYPOINT ["sh", "entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]