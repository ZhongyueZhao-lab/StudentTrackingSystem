ARG PYTHON_VERSION=3.9

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    pip install gunicorn && \
    pip install PyMySQL && \
    pip install dbbackup && \
    rm -rf /root/.cache/
COPY . /code

EXPOSE 8000

CMD ["gunicorn","--bind",":8000","--workers","2","student_tracking_system.wsgi:application"]
