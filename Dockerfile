ARG PYTHON_VERSION=3.11
ARG DEBIAN_VERSION=bullseye

FROM python:${PYTHON_VERSION}-slim-${DEBIAN_VERSION}
ENV APP_FOLDER=/var/www/app
ENV PYTHONUNBUFFERED 1
WORKDIR ${APP_FOLDER}
COPY requirements.txt requirements.txt
RUN : "installing pip deps" \ 
    && pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "[::]:8000"]
