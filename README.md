# Dolibarr ERP - Gestion RH

> Installation et configuration de Dolibarr ERP pour la gestion des Ressources Humaines (conges, paie, employes) - Projet de stage QA

## Table des matieres

- [Presentation](#presentation)
- [Prerequis](#prerequis)
- [Installation sous Windows](#installation-sous-windows)
- [Configuration initiale](#configuration-initiale)
- [Modules RH actives](#modules-rh-actives)
- [Tests fonctionnels](#tests-fonctionnels)
- [Structure du projet](#structure-du-projet)
- [Auteur](#auteur)

## Presentation

Dolibarr est un ERP/CRM open source permettant de gerer les processus metier d'une entreprise. Ce projet se concentre sur la configuration des modules RH pour:
- Gestion des employes
- Gestion des conges et absences
- Gestion de la paie
- Suivi des contrats de travail

## Prerequis

- Windows 10/11
- DoliWamp 21.0.4 (package tout-en-un incluant Apache, MySQL, PHP)
- Navigateur web moderne (Chrome, Firefox, Edge)
- 500 Mo d'espace disque minimum

## Installation sous Windows

### Etape 1: Telecharger DoliWamp

1. Aller sur [SourceForge Dolibarr](https://sourceforge.net/projects/dolibarr/files/Dolibarr%20installer%20for%20Windows%20%28DoliWamp%29/)
2. Telecharger la derniere version: `DoliWamp-21.0.4.exe` (121 Mo)

### Etape 2: Installer DoliWamp

1. Executer `DoliWamp-21.0.4.exe` en tant qu'administrateur
2. Accepter les termes de la licence
3. Choisir le repertoire d'installation (defaut: `C:\DoliWamp`)
4. Laisser les ports par defaut (Apache: 80, MySQL: 3306)
5. Definir le mot de passe root MySQL
6. Terminer l'installation

### Etape 3: Demarrer les services

1. Lancer DoliWamp depuis le menu Demarrer
2. Verifier que Apache et MySQL sont demarres (icones verts)
3. Ouvrir le navigateur: `http://localhost/dolibarr`

### Etape 4: Configuration initiale Dolibarr

1. Suivre l'assistant d'installation web
2. Configurer la base de donnees:
   - Serveur: `localhost`
   - Nom de la base: `dolibarr`
   - Utilisateur: `root`
   - Mot de passe: (celui defini a l'installation)
3. Creer le compte administrateur
4. Terminer l'installation

## Configuration initiale

### Informations de connexion par defaut

| Parametre | Valeur |
|-----------|--------|
| URL | http://localhost/dolibarr |
| Admin | admin |
| Base de donnees | dolibarr |

### Chemins importants

```
C:\DoliWamp\
|-- www/
|   |-- dolibarr/          # Application web
|-- documents/             # Documents generes (PDF, exports)
|-- mysql/                 # Base de donnees
|-- apache/                # Serveur web
```

## Modules RH actives

Pour activer les modules RH:
1. Aller dans **Accueil > Configuration > Modules**
2. Activer les modules suivants:

| Module | Description |
|--------|-------------|
| Utilisateurs & Groupes | Gestion des utilisateurs |
| Ressources Humaines | Fiches employes, contrats |
| Conges | Gestion des conges et absences |
| Feuilles de temps | Suivi du temps de travail |
| Salaires | Gestion de la paie |
| Notes de frais | Remboursement des frais |

## Tests fonctionnels

### Scenarios de test

1. **Test creation employe**
   - Creer une fiche employe complete
   - Verifier les informations enregistrees

2. **Test demande de conge**
   - Soumettre une demande de conge
   - Valider/Refuser la demande
   - Verifier le solde de conges

3. **Test bulletin de paie**
   - Generer un bulletin de paie
   - Verifier les calculs
   - Exporter en PDF

## Structure du projet

```
dolibarr-erp-rh/
|-- README.md              # Ce fichier
|-- docs/
|   |-- installation.md    # Guide d'installation detaille
|   |-- configuration.md   # Configuration des modules
|-- tests/
|   |-- plan_test.md       # Plan de test
|   |-- scenarios/         # Scenarios de test
|-- screenshots/           # Captures d'ecran
```

## Auteur

**Ahmed Ayadi**
- Stage QA Automation
- Date: Novembre 2025

## Licence

Ce projet est sous licence GPL (comme Dolibarr).

---

*Documentation generee dans le cadre du projet de stage QA*
