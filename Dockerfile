FROM python:3.9-slim 
# because slimmer is better
WORKDIR /app

# finally doing this shit in professional way
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONUNBUFFERED=1
CMD ["python3", "bot.py"]
