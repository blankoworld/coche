# Présentation

Coche est un assistant de suivi de recherche d'emploi. Comme un outil de prospect (utilisé par un commercial), mais à destination des personnes à la recherche d'un emploi.

Son but est donc d'enregistrer l'évolution de votre recherche d'emploi.

Savoir quelle entreprise a été contactée, de quelle manière, à quelle date, etc.

# Dépendances

* docker
* docker-compose
* php 7.4|8.0 avec les extensions suivantes :
  * pdo\_mysql
  * mysqli

# Dépendances applicatives

```bash
cd www
composer install
```

# Installation

`docker-compose up -d`

# Utilisation

```bash
cd www
php artisan serve
```

Aller sur http://localhost:8000/

