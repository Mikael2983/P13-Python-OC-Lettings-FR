# Orange County Lettings

**Site web de gestion de locations pour Orange County.**

---
## 📌 Résumé

Ce projet est une application Django permettant de gérer des profils et des locations pour Orange County. Il inclut une interface utilisateur, un panneau d'administration, et une base de données SQLite.

---

## 🛠 Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce dépôt
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.10 ou supérieure

> ⚠️ **Note** : Les instructions ci-dessous supposent que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

---

### 📥 Installation

#### 1. Cloner le dépôt
Depuis le répertoire de destination, exécuter:
```bash
git clone https://github.com/Mikael2983/P13-Python-OC-Lettings-FR.git
cd P13-Python-OC-Lettings-FR
```
#### 2. Créer l'environnement virtuel
```bash
python -m venv venv
```
Puis activer la: 
Sous Unix/MacOS
```bash
source venv/bin/activate
```
Sous Windows:
```bash  
venv/Scripts/activate
```
Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu :
```bash
sudo apt-get install python3-venv
```

#### 3. Installer les dépendances
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
### 🚀 Lancer le site
```bash
python manage.py runserver
```
Aller sur http://localhost:8000 dans un navigateur.


Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

```bash
.tables
pragma table_info(oc_lettings_profile);
SELECT * FROM oc_lettings_profile LIMIT 5;
.quit
```

### 🧹 Linting
```bash
flake8
```
### 🧪 Tests
```bash
pytest
```
### 🗃 Base de données
```bash
sqlite3 oc-lettings-site.sqlite3
```
Exemples de commandes :
```bash
.tables                          -- Lister les tables
pragma table_info(oc_lettings_profile);  -- Voir les colonnes de la table "profile"
SELECT * FROM oc_lettings_profile LIMIT 5;  -- Voir les 5 premiers profils
.quit                            -- Quitter
```

## 🔐 Panel d'administration

- Aller sur http://localhost:8000/admin

- Identifiants par défaut :
    - Utilisateur : admin
    - Mot de passe : Abc1234!

## 🔄 CI/CD
Ce projet utilise GitHub Actions pour :

- Exécuter les tests et le linting à chaque push/pull request.
- Vérifier la couverture de test (> 80%).
- Générer un rapport de couverture HTML (disponible dans les artefacts du workflow).


📄 Fichier de configuration : .github/workflows/django_ci.yml


## 🤝 Contribution
Les contributions sont les bienvenues ! Pour contribuer :

- Forkez le dépôt.
- Créez une branche (git checkout -b feature/ma-nouvelle-fonctionnalité).
- Commitez vos changements (git commit -m "Ajout de ma fonctionnalité").
- Poussez la branche (git push origin feature/ma-nouvelle-fonctionnalité).
- Ouvrez une Pull Request.


## 📂 Structure du projet
```bash
Python-OC-Lettings-FR/
├── oc_lettings_site/          # Configuration principale de l'application Django
│   ├── tests/                 # Tests unitaires et d'intégration pour le projet global
│   ├── apps.py                # Configuration de l'application Django
│   ├── asgi.py                # Configuration ASGI pour les serveurs asynchrones
│   ├── settings.py            # Paramètres de configuration (BASE_DIR, INSTALLED_APPS, DATABASES, etc.)
│   ├── urls.py                # Routage principal des URLs du projet
│   ├── views.py                # Vues globales (si applicable)
│   └── wsgi.py                 # Configuration WSGI pour les serveurs web classiques
│
├── lettings/                  # Module de gestion des locations
│   ├── tests/                 # Tests unitaires pour le module "lettings"
│   ├── templates/             # Templates HTML spécifiques au module "lettings"
│   ├── admin.py               # Configuration de l'interface d'administration pour les locations
│   ├── apps.py                # Configuration de l'application "lettings"
│   ├── models.py              # Modèles de données pour les locations
│   ├── urls.py                # Routage des URLs spécifiques au module "lettings"
│   └── views.py               # Vues pour les fonctionnalités liées aux locations
│
├── profiles/                  # Module de gestion des profils utilisateurs
│   ├── tests/                 # Tests unitaires pour le module "profiles"
│   ├── templates/             # Templates HTML spécifiques au module "profiles"
│   ├── admin.py               # Configuration de l'interface d'administration pour les profils
│   ├── apps.py                # Configuration de l'application "profiles"
│   ├── models.py              # Modèles de données pour les profils utilisateurs
│   ├── urls.py                # Routage des URLs spécifiques au module "profiles"
│   └── views.py               # Vues pour les fonctionnalités liées aux profils
│
├── static/                    # Fichiers statiques (CSS, JS, images) partagés par l'ensemble du projet
├── templates/                 # Templates HTML partagés par l'ensemble du projet
├── .env.example               # Fichier d'exemple de variable d'environement. 
├── manage.py                  # Script de gestion Django (lancement du serveur, migrations, etc.)
├── requirements.txt           # Liste des dépendances Python nécessaires au projet
└── README.md                  # Documentation du projet
```
---

### 🐳 Déploiement avec Docker

Une image Docker prête à l’emploi est disponible: mikael2983/python_lettings_fr:latest
Elle est automatiquement mise à jour à chaque commit ou pull request sur la branche main
Exécutez le conteneur localement:
```bash
docker pull mikael2983/python_lettings_fr:latest
docker run -p 8000:8000 mikael2983/python_lettings_fr
```

Accédez à l’application sur: http://127.0.0.1:8000/

⚠️ Note : Assurez-vous que le port 8000 est disponible et que les variables d'environnement (comme SECRET_KEY et DEBUG) sont correctement configurées.

## 📜 Licence
Ce projet est sous licence MIT.