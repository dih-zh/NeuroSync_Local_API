FROM nvidia/cuda:12.8.1-runtime-ubuntu24.04

RUN apt-get update && \
  apt-get -y install software-properties-common curl && \
  add-apt-repository ppa:deadsnakes/ppa && \
  apt-get install -y python3.12 python3.12-venv --no-install-recommends && \
  rm -rf /var/lib/apt/lists/*

RUN python3.12 -m venv /opt/venv

COPY ./requirements.txt /
RUN /opt/venv/bin/pip install --no-cache-dir -r /requirements.txt && \
  rm /requirements.txt

RUN mkdir /app

# Copy app 
COPY ./neurosync_local_api.py /app/neurosync_local_api.py
COPY ./utils /app/utils

WORKDIR /app
EXPOSE 5000
# CMD ["/opt/venv/bin/gunicorn", "neurosync_local_api:app", "--timeout=0", "--preload", \
#   "--workers=1", "--worker-class=gevent", "--threads=4", "--bind=0.0.0.0:5000"]
CMD ["/opt/venv/bin/python", "neurosync_local_api.py"]
