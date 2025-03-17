FROM europe-docker.pkg.dev/vertex-ai/prediction/pytorch-cpu.2-4:latest

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt && \
  rm /requirements.txt

RUN mkdir /app

# Copy app 
COPY ./neurosync_local_api.py /app/neurosync_local_api.py
COPY ./utils /app/utils

# run server with gunicorn
WORKDIR /app
EXPOSE 5000
CMD ["gunicorn", "neurosync_local_api:app", "--timeout=0", "--preload", \
  "--workers=1", "--threads=4", "--bind=0.0.0.0:5000"]
