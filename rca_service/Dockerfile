FROM python:3.11-slim
WORKDIR /app
RUN pip install requests flask
COPY rca.py .
EXPOSE 8000
CMD ["python", "rca.py"]