# Utilise une image officielle Python
FROM python:3.11

# Copie le code dans le conteneur
WORKDIR /app
COPY . .

# Installe les dépendances
RUN pip install -r requirements.txt

# Commande pour démarrer l’appli
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
