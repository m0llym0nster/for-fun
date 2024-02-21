FROM python:3.11-alpine
COPY requirements.txt .
COPY pso_sectid.py .
COPY main.py . 
RUN pip install -r requirements.txt
CMD ["python","./main.py"]
