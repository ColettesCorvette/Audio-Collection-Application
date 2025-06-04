FROM python:3.11

# Ajoute un utilisateur non-root
RUN useradd -m appuser
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Droits d'accès sur recordings
RUN mkdir -p /app/recordings && chown -R appuser:appuser /app

USER appuser

CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]

