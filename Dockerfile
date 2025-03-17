FROM europe-docker.pkg.dev/vertex-ai/prediction/pytorch-cpu.2-4:latest

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt


# Copy app 
COPY ./neurosync_local_api.py /neurosync_local_api.py
COPY ./utils /utils

# run server with gunicorn
WORKDIR /
EXPOSE 5000
CMD ["gunicorn", "neurosync_local_api:app", "--timeout=0", "--preload", \
  "--workers=1", "--threads=4", "--bind=0.0.0.0:5000"]
