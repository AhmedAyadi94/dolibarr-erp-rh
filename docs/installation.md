# Guide d'Installation - Dolibarr ERP RH

## Table des matières
- [Pré-requis](#pré-requis)
- [Installation sur Windows](#installation-sur-windows)
- [Installation sur Linux (CentOS 7)](#installation-sur-linux-centos-7)
- [Configuration post-installation](#configuration-post-installation)
- [Résolution des problèmes](#résolution-des-problèmes)

## Pré-requis

### Pour Windows
- **Système d'exploitation**: Windows 10 ou 11 (64-bit)
- **Espace disque**: Minimum 500 Mo libres
- **RAM**: Minimum 2 Go (4 Go recommandé)
- **Navigateur**: Chrome, Firefox, Edge (dernière version)

### Pour Linux (CentOS 7)
- **Système d'exploitation**: CentOS 7.x (64-bit)
- **Espace disque**: Minimum 1 Go libre
- **RAM**: Minimum 2 Go (4 Go recommandé)
- **Accès root** ou utilisateur avec privilèges sudo

## Installation sur Windows

### Étape 1: Téléchargement

1. Aller sur [SourceForge - Dolibarr](https://sourceforge.net/projects/dolibarr/files/)
2. Télécharger la dernière version:
   - **Fichier**: `DoliWamp-21.0.4.exe`
   - **Taille**: ~121 Mo

### Étape 2: Installation

1. **Exécuter l'installeur**
   - Double-cliquer sur DoliWamp-21.0.4.exe
   - Clic droit > Exécuter en tant qu'administrateur

2. **Assistant d'installation**
   - Accepter les termes de la licence
   - Choisir le répertoire d'installation (défaut: `C:\DoliWamp`)
   - Configurer les ports: Apache: 80, MySQL: 3306

3. **Configuration MySQL**
   - Définir un mot de passe root MySQL
   - Noter ce mot de passe

## Installation sur Linux (CentOS 7)

### Mise à jour du système
```bash
sudo yum update -y
```

### Installation d'Apache
```bash
sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
```

### Installation de PHP
```bash
sudo yum install php php-mbstring php-curl php-gd php-mysql -y
sudo systemctl restart httpd
```

### Installation de MariaDB
```bash
sudo yum install mariadb-server -y
sudo systemctl start mariadb
sudo mysql_secure_installation
```

### Création de la base de données
```sql
CREATE DATABASE dolibarr;
CREATE USER 'dolibarr_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON dolibarr.* TO 'dolibarr_user'@'localhost';
FLUSH PRIVILEGES;
```

## Configuration post-installation

1. Accéder à: `http://localhost/dolibarr`
2. Suivre l'assistant de configuration
3. Configurer la connexion à la base de données
4. Créer le compte administrateur

---
**Auteur**: Ahmed Ayadi - Stage QA Automation
**Date**: Décembre 2025
