FROM python:3.11-alpine AS build

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Second stage
FROM python:3.11-alpine

WORKDIR /app

# Copy only necessary files from the previous stage
COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .

EXPOSE 8000

CMD ["python", "py-app/app.py"]