FROM python:3.9.16
WORKDIR usr/src/app
# includ requirements.txt
COPY ./ ./
RUN pip install --no-cache-dir -r requirements.txt
# EXPOSE 8000
CMD ["python3", "ml.py"]