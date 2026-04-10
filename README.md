# SAE4A_2026_JPO-TRACKER-Backend

API REST Flask pour la gestion des visiteurs des Journées Portes Ouvertes de l'IUT de Montreuil.

---

## Prérequis

- Python 3.10+
- MongoDB (local ou Atlas)

---

## Installation

```bash
# Cloner le projet
git clone <url-du-repo>
cd backend

# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

---

## Configuration

Créer un fichier `.env` à la racine du projet :

```env
MONGO_URI=mongodb://localhost:27017/jpo
SECRET_KEY=une_cle_secrete_longue_et_aleatoire
ADMIN_PASSWORD_HASH=$2b$12$...   # hash bcrypt du mot de passe admin
```

Pour générer le hash du mot de passe admin :

```python
import bcrypt
print(bcrypt.hashpw(b"VotreMotDePasse", bcrypt.gensalt()).decode())
```

---

## Lancer le serveur

```bash
python -m flask run
```

Le serveur démarre sur `http://localhost:5000`.

---

## Structure du projet

```
backend/
├── controllers/
│   ├── auth_controler.py       # Routes d'authentification
│   ├── visiteur_controler.py   # Routes visiteurs
│   └── export_controler.py     # Routes d'export CSV
├── service/
│   ├── auth_service.py         # Logique auth + middleware JWT
│   ├── visiteur_service.py     # Logique métier visiteurs
│   └── export_service.py       # Génération des CSV
├── dtos/
│   └── visiteur_dto.py         # DTO court et long
├── extension.py                # Instance PyMongo
├── app.py                      # Point d'entrée Flask
├── requirements.txt
└── .env
```

---

## Endpoints

### Authentification

| Méthode | Route | Description | Auth |
|---------|-------|-------------|------|
| POST | `/auth/login` | Connexion admin | Non |
| PUT | `/auth/changer-mot-de-passe` | Changer le mot de passe | ✅ JWT |

### Visiteurs

| Méthode | Route | Description | Auth |
|---------|-------|-------------|------|
| GET | `/visiteurs/` | Liste complète | ✅ JWT |
| GET | `/visiteurs/full` | Liste complète (DTO long) | Non |
| GET | `/visiteurs/filtrer` | Liste filtrée + pagination | ✅ JWT |
| GET | `/visiteurs/<id>` | Détail d'un visiteur | ✅ JWT |
| GET | `/visiteurs/dept/<dept>` | Visiteurs par département | ✅ JWT |
| POST | `/visiteurs/` | Créer un visiteur | Non |
| PUT | `/visiteurs/<id>` | Modifier un visiteur | ✅ JWT |
| DELETE | `/visiteurs/<id>` | Supprimer un visiteur | ✅ JWT |
| DELETE | `/visiteurs/` | Supprimer tous les visiteurs | ✅ JWT |

#### Paramètres de filtre (`/visiteurs/filtrer`)

| Paramètre | Type | Description |
|-----------|------|-------------|
| `search` | string | Recherche nom / prénom / email |
| `departement` | string | Formation intéressée |
| `formationOrigine` | string | Type de formation d'origine |
| `reorientation` | boolean | Uniquement les réorientations |
| `situationParticuliere` | boolean | Uniquement situations particulières |
| `page` | int | Numéro de page (défaut : 1) |
| `limit` | int | Résultats par page (défaut : 10) |

### Export

| Méthode | Route | Description | Auth |
|---------|-------|-------------|------|
| GET | `/export/visiteurs/csv` | Export complet en CSV | Non |
| GET | `/export/visiteurs/emails/csv` | Export emails en CSV | Non |

Les mêmes paramètres de filtre que `/visiteurs/filtrer` sont acceptés.

---

## Authentification JWT

Les routes protégées nécessitent un header :

```
Authorization: Bearer <token>
```

Le token est obtenu via `POST /auth/login` et expire après **8 heures**.

---

## Dépendances principales

| Package | Rôle |
|---------|------|
| Flask | Framework web |
| Flask-PyMongo | Connexion MongoDB |
| Flask-Cors | Gestion CORS |
| PyJWT | Génération / vérification des tokens JWT |
| bcrypt | Hashage du mot de passe admin |
| python-dotenv | Chargement du fichier `.env` |
| phonenumbers | Validation des numéros de téléphone |
