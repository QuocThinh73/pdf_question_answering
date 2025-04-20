FROM python:3.13

WORKDIR /app

COPY requirements.txt /app
COPY src/ /app/src/
COPY data_source/ /app/data_source/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]