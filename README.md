# Présentation

Coche est un assistant de suivi de recherche d'emploi. Comme un outil de prospect (utilisé par un commercial), mais à destination des personnes à la recherche d'un emploi.

Son but est donc d'enregistrer l'évolution de votre recherche d'emploi.

Savoir quelle entreprise a été contactée, de quelle manière, à quelle date, etc.

# Dépendances

Ce programme dépend de :

  * python3
  * python3-markdown
  * python3-pip
  * python3-virtualenv

Sur une distribution basée sur Debian, tapez la commande suivante : 

    sudo apt-get install -y python3 python3-virtualenv python3-pip

Cela installe l'ensemble des dépendances.

# Dépendances applicatives

Lancer : 

    ./dependancies.sh

Patienter.

Vous êtes désormais dans un environnement virtuel avec les dépendances de l'application installées localement.

Pour quitter l'environnement virtuel, tapez simplement : ```deactivate```.

# Utilisation

Lancer : 

    python app.py

Ouvrir un navigateur Web sur la [page d'accueil de Coche](http://localhost:5000/)
