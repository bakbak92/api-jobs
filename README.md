# Job API

API REST FastAPI pour lister, filtrer et gérer des offres d'emploi, avec une analyse de description via OpenAI.

## Prérequis

- Python 3.11+
- Une clé API OpenAI (pour `POST /jobs/analyze`)

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Copiez `.env.template` vers `.env` et renseignez les variables :

```env
APP_NAME=Job api
DEBUG=true
OPENAI_API_KEY=sk-...
```

`OPENAI_API_KEY` est obligatoire.

## Lancement

```bash
uvicorn main:app --reload
```

L'API est disponible sur [http://127.0.0.1:8000](http://127.0.0.1:8000).

Documentation interactive :

- Swagger UI : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc : [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Endpoints

| Méthode | Chemin | Description |
| --- | --- | --- |
| `GET` | `/` | Santé de l'API |
| `GET` | `/jobs/` | Liste filtrée des offres |
| `GET` | `/jobs/{id}` | Détail d'une offre |
| `POST` | `/jobs/` | Création d'une offre |
| `PATCH` | `/jobs/{id}` | Mise à jour partielle |
| `DELETE` | `/jobs/{id}` | Suppression |
| `POST` | `/jobs/analyze` | Extraction des compétences à partir d'une description |

### Filtres (`GET /jobs/`)

Paramètres de query optionnels :

| Paramètre | Type | Défaut | Contraintes |
| --- | --- | --- | --- |
| `title` | string | — | recherche partielle, insensible à la casse |
| `company` | string | — | recherche partielle |
| `location` | string | — | recherche partielle |
| `salary_min` | int | `0` | `>= 0` |
| `skill` | string | — | correspondance partielle dans la liste des skills |
| `remote` | bool | — | `true` / `false` |
| `limit` | int | `10` | entre `10` et `100` |

Exemple :

```bash
curl "http://127.0.0.1:8000/jobs/?title=engineer&remote=true&limit=10"
```

### Création (`POST /jobs/`)

```json
{
  "title": "Backend Engineer",
  "company": "Acme",
  "location": "Paris",
  "salary": 65000,
  "skills": ["Python", "FastAPI"],
  "remote": true
}
```

### Analyse (`POST /jobs/analyze`)

Envoie une description de poste ; le modèle `gpt-4o-mini` en extrait les compétences.

```json
{
  "description": "Nous recherchons un développeur Python avec FastAPI, PostgreSQL et Docker."
}
```

Réponse :

```json
{
  "skills": ["Python", "FastAPI", "PostgreSQL", "Docker"]
}
```

Les données sont stockées en mémoire (`db/data.py`) : elles sont réinitialisées au redémarrage du serveur.

## Structure

```text
api-jobs/
├── main.py                 # Application FastAPI et middleware de timing
├── config.py               # Settings (pydantic-settings + .env)
├── routers/jobs.py         # Routes HTTP
├── services/job_service.py # Logique métier et appel OpenAI
├── schemas/job_schema.py   # Modèles Pydantic
└── db/data.py              # Jeu de données en mémoire
```

Chaque réponse HTTP inclut un en-tête `X-Process-Time` (durée de traitement).
