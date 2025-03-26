FROM pytorch/pytorch:2.6.0-cuda12.6-cudnn9-runtime

COPY ./requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt && \
  rm /requirements.txt

RUN mkdir /app

# Copy app 
COPY ./neurosync_local_api.py /app/neurosync_local_api.py
COPY ./utils /app/utils

WORKDIR /app
EXPOSE 5000
# CMD ["/opt/venv/bin/gunicorn", "neurosync_local_api:app", "--timeout=0", "--preload", \
#   "--workers=1", "--worker-class=gevent", "--threads=4", "--bind=0.0.0.0:5000"]
CMD ["python", "neurosync_local_api.py"]

