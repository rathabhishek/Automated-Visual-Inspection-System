FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install minimal system deps required by OpenCV wheels
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       libgl1 \
       libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements-dev.txt ./

RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements-dev.txt

COPY . /app

CMD ["python", "color_detection.py", "-i", "./sample.jpg"]
