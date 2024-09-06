FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN reflex init

ENV PORT 8080

EXPOSE 8080

# Ejecutamos la aplicación completa
CMD reflex run --env prod --port $PORT