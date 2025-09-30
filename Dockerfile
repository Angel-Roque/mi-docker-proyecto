FROM python:3.9-slim

WORKDIR /app

COPY apli.py /app
COPY templates/ /app/templates
COPY static/ /app/static

RUN pip install --no-cache-dir flask requests

EXPOSE 5000

CMD ["python3"," apli.py"]

