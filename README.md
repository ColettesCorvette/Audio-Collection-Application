Audio Collection Application
===========================

Cette application web permet de collecter anonymement des enregistrements audio de participants lisant des phrases affichées à l'écran.
Elle facilite la recherche et la collecte de données vocales dans le respect de la vie privée, sans jamais demander de donnée personnelle.

---------------------------
Fonctionnalités principales
---------------------------
- Interface web simple et efficace (Streamlit)
- Saisie anonyme d’informations démographiques (âge, genre, consentement)
- Choix du nombre de phrases à lire pour chaque session
- Affichage de phrases choisies aléatoirement et sans doublons parmi celles présentes dans `sentences.txt`
- Enregistrement audio phrase par phrase
- Réécoute immédiate après chaque enregistrement
- Arrêt anticipé de la session possible (les fichiers déjà enregistrés sont conservés)
- Aucune information personnelle collectée
- Déploiement rapide avec Docker (et Docker Compose, compatible reverse proxy)

------------------------
Installation & Lancement
------------------------
1. Prérequis
   - Docker installé sur votre machine
   - (Facultatif pour dev local) Python 3.8+ et pip

2. Cloner le dépôt
   git clone https://github.com/ColettesCorvette/Audio-Collection-Application.git
   cd Audio-Collection-Application

3. Préparer les phrases à lire
   Modifiez le fichier sentences.txt pour ajouter ou remplacer les phrases à lire, une phrase par ligne (sans numérotation, ni guillemets).
   Exemple de contenu pour sentences.txt :
   Bonjour, comment allez-vous ?
   Le chat dort sur le canapé.
   Il fait beau aujourd'hui.
   ...
   (Jusqu'à 100 phrases ou plus)

4. Démarrer l’application avec Docker Compose
   docker compose up --build
   L’application sera accessible sur http://localhost:8501
   Les enregistrements audio sont sauvegardés automatiquement dans le dossier recordings/ de votre projet.

5. Récupérer les fichiers audio
   Tous les fichiers générés sont dans le dossier recordings/ du dépôt, visible sur votre machine (grâce au volume Docker).

---------------------------
Architecture & Workflow
---------------------------
- Accueil : L’utilisateur commence une session
- Formulaire : Renseigne âge, genre, consentement, nombre de phrases à enregistrer
- Sélection aléatoire : L’application pioche N phrases différentes dans sentences.txt (ordre aléatoire)
- Session d’enregistrement : L’utilisateur lit chaque phrase, enregistre et valide son audio, puis passe à la suivante
- Fin ou arrêt anticipé : Retour à l’accueil, tous les fichiers déjà enregistrés sont sauvegardés

-------------------------
Sécurité & Anonymat
-------------------------
Respect de la vie privée
- L’application ne collecte aucune donnée personnelle (pas de nom, pas d’email, pas d’IP, etc.)
- Seules les informations minimales (âge, genre, consentement explicite) sont demandées au début de chaque session
- Les fichiers sont nommés de manière anonyme : age_genre_phraseX.wav

Consentement
- L’utilisateur doit obligatoirement donner son consentement explicite avant de commencer

Sécurité technique
- L’application tourne entièrement dans un conteneur Docker, ce qui limite les risques d’accès non autorisé au système hôte
- Seul le port 8501 (HTTP) est exposé par défaut
- Il est recommandé, en production, de placer l’application derrière un reverse proxy HTTPS (Caddy, NGINX)
- Le fichier .dockerignore protège l’image Docker en excluant les fichiers inutiles ou sensibles

Bonnes pratiques
- Aucun mot de passe ou clé API n’est utilisé ni stocké
- Les enregistrements sont accessibles uniquement aux administrateurs du serveur local
- Pensez à nettoyer le dossier recordings/ régulièrement selon la politique de conservation des données
