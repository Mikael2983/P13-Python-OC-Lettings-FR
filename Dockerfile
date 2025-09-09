# choisir une image Python
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier uniquement le fichier requirements pour optimiser le cache
COPY requirements.txt .

# Installer les dépendances
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copier tout le projet
COPY . .

# Exposer le port 8000 pour Django
EXPOSE 8000

ENV DEBUG=False

CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000"]
