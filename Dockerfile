FROM python:3.11-alpine
COPY for-fun .
RUN pip install -r requirements.txt
CMD ["python","./main.py"]
