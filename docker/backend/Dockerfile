FROM python:3.5

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -U pip setuptools && \
    pip install --no-cache-dir -Ur requirements.txt


COPY app.py .

ENV PYTHONPATH=/usr/src/app
CMD python app.py
