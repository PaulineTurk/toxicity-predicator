# Base Python légère
FROM python:3.11

# Dossier de travail dans le container
WORKDIR /app

# Installer Poetry
RUN pip install poetry

# Copier les fichiers de dépendances
COPY pyproject.toml poetry.lock ./

# Installer toutes les dépendances Python sans créer de virtualenv
RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi --no-root

# Copier le reste du projet
COPY . .

# Commande par défaut
CMD ["python", "test/test_poetry_install.py"]