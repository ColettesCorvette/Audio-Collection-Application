# Audio Collection Application

Ce projet est une application web permettant de collecter anonymement des enregistrements audio de participants qui lisent des phrases à l'écran.
Elle est conçue pour faciliter la recherche et la collecte de données vocales tout en respectant la vie privée.

---

## 🛠️ Fonctionnalités

- Interface web simple (Streamlit)
- Collecte des infos démographiques **anonymes** (âge, genre, consentement)
- Sélection du nombre de phrases à lire (optionnel)
- Enregistrement audio phrase par phrase
- Réécoute immédiate possible
- Arrêt anticipé de la session possible
- **Aucune information personnelle collectée**
- Déploiement facile via Docker (et Docker Compose, possibilité de reverse proxy)

---

## 🚀 Installation & Lancement

### 1. **Prérequis**

- [Docker](https://www.docker.com/products/docker-desktop/) installé sur votre machine
- (Facultatif pour dev local) Python 3.8+

### 2. **Cloner le dépôt**

```bash
git clone git@github.com:ColettesCorvette/Audio-Collection-Application.git
cd Audio-Collection-Application
```

### 3. **Préparer les phrases à lire**

Modifiez ou remplacez le fichier sentences.txt pour ajouter vos phrases, une phrase par ligne.


### 4. Démarrer l’application avec Docker Compose

```bash
docker compose up --build
```

L’application sera accessible sur https://localhost
Les enregistrements seront sauvegardés dans le dossier recordings/.

🛡️ Sécurité & Anonymat
Respect de la vie privée

    L’application ne collecte aucune donnée personnelle (pas de nom, email, IP, etc.).

    Seules les informations minimales (âge, genre, consentement explicite) sont demandées.

    Chaque fichier audio est stocké anonymement avec un nom du type age_genre_phraseX.wav.

    Les réponses sont stockées localement, sans transmission vers un serveur tiers.

Consentement

    L’utilisateur doit obligatoirement donner son consentement explicite avant de participer.

Sécurité technique

    L’application tourne dans un conteneur Docker, ce qui limite les risques d’accès non autorisé au système hôte.

    Aucun service inutile n’est exposé ; seul le port 8501 (http) est ouvert par défaut.

    Pour un usage en production, il est recommandé de placer l’application derrière un reverse proxy (Caddy) et d’utiliser HTTPS.

    Un .dockerignore est présent pour ne pas embarquer de fichiers sensibles dans l’image Docker.

Bonnes pratiques

    Aucun mot de passe ou clé API n’est utilisé ou stocké.

    Les enregistrements sont accessibles uniquement par les administrateurs du serveur local.

    Il est recommandé de nettoyer le dossier recordings/ régulièrement selon les besoins du projet.




