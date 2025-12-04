# Guide de Configuration - Dolibarr ERP RH

## Introduction
Ce guide détaille la configuration des modules RH de Dolibarr pour optimiser la gestion des ressources humaines.

## Configuration de base

### 1. Paramètres société
**Chemin:** Accueil > Configuration > Société

```
Nom de l'entreprise: [Votre entreprise]
Adresse: [Adresse complète]
Code postal: [Code]
Ville: [Ville]
Pays: France
Téléphone: [Numéro]
Email: [contact@entreprise.fr]
```

### 2. Utilisateurs et permissions

#### Créer un utilisateur
**Chemin:** Accueil > Utilisateurs & Groupes > Nouvel utilisateur

**Informations obligatoires:**
- Login
- Mot de passe
- Nom/Prénom
- Email

#### Groupes de permissions
Créer des groupes selon les rôles:

**Groupe "RH Administrateur":**
- Lecture/Écriture: Ressources Humaines
- Lecture/Écriture: Congés
- Lecture/Écriture: Salaires
- Lecture/Écriture: Notes de frais

**Groupe "Employé":**
- Lecture: Propre fiche employé
- Lecture/Écriture: Propres congés
- Lecture/Écriture: Propres notes de frais

**Groupe "Manager":**
- Lecture: Toutes fiches employés
- Validation: Congés équipe
- Validation: Notes de frais équipe

## Configuration des modules RH

### Module Ressources Humaines

**Activation:**
1. Accueil > Configuration > Modules
2. Rechercher "Ressources Humaines"
3. Cliquer sur "Activer"

**Configuration:**
```
Accueil > Configuration > RH

Options:
☑ Activer les fiches employés
☑ Activer la gestion des contrats
☑ Activer le suivi des absences
☑ Activer l'historique des postes
```

**Champs personnalisés employés:**
- Date d'embauche
- Type de contrat (CDI/CDD/Stage)
- Département
- Poste
- Manager direct
- Numéro sécurité sociale

### Module Congés

**Configuration:**
```
Accueil > Configuration > Congés

Paramètres généraux:
- Solde initial: 25 jours/an (RTT inclus)
- Report maximum: 5 jours
- Préavis minimum: 15 jours

Types de congés:
1. Congés payés (CP)
2. RTT
3. Congés sans solde
4. Congé maladie
5. Congé maternité/paternité
6. Formation
```

**Workflow de validation:**
```
1. Employé soumet demande
   ↓
2. Manager valide (ou rejette)
   ↓
3. RH Admin valide définitivement
   ↓
4. Notification envoyée à l'employé
```

### Module Salaires

**Configuration:**
```
Accueil > Configuration > Salaires

Éléments de paie:
☑ Salaire de base
☑ Primes
☑ Heures supplémentaires
☑ Indemnités transport
☑ Tickets restaurant
☑ Mutuelle
```

**Périodicité:**
- Fréquence: Mensuelle
- Date de paiement: Dernier jour du mois
- Date d'édition bulletin: 25 du mois

### Module Notes de frais

**Configuration:**
```
Accueil > Configuration > Notes de frais

Types de frais:
1. Transport (Km, Train, Avion)
2. Hébergement
3. Restauration
4. Téléphone
5. Fournitures
6. Autres

Barèmes kilométriques (2025):
- < 5000 km: 0,575 €/km
- 5001-20000 km: 0,345 €/km
- > 20000 km: 0,317 €/km
```

## Configuration email

### Serveur SMTP
**Chemin:** Accueil > Configuration > Emails

```
Serveur SMTP: smtp.office365.com
Port: 587
Sécurité: STARTTLS
Authentification: Oui
Login: notifications@entreprise.fr
Mot de passe: [mot_de_passe]
```

### Templates emails

**Validation congé:**
```
Objet: Congé validé du {DATE_DEBUT} au {DATE_FIN}
Corps:
Bonjour {PRENOM},

Votre demande de congé a été validée:
- Du: {DATE_DEBUT}
- Au: {DATE_FIN}
- Type: {TYPE_CONGE}
- Durée: {NB_JOURS} jours

Bon repos!

L'équipe RH
```

## Configuration des droits d'accès

### Matrice des droits

| Module | Admin RH | Manager | Employé |
|--------|----------|---------|---------|
| Fiches employés | RW | R (équipe) | R (soi) |
| Congés | RW | RW (équipe) | RW (soi) |
| Salaires | RW | - | R (soi) |
| Notes de frais | RW | RW (équipe) | RW (soi) |
| Contrats | RW | R | R (soi) |

**Légende:**
- R: Lecture
- W: Écriture
- RW: Lecture et écriture
- -: Aucun accès

## Configuration avancée

### Workflows automatiques

**Rappel congés non pris:**
```php
// Cron à configurer
Fréquence: Mensuel (1er du mois)
Script: rappel_conges.php
Action: Envoyer email aux employés
        avec solde > 10 jours
```

**Validation automatique notes de frais < 50€:**
```
Accueil > Configuration > Workflows
☑ Auto-valider notes < 50€
☑ Notifier manager si > 50€
```

### Intégrations

**Export comptabilité:**
```
Format: CSV/Excel
Champs: Matricule, Nom, Salaire brut, 
        Cotisations, Net à payer
Fréquence: Mensuelle
```

**Import données RH:**
```
Format: CSV
Colonnes obligatoires:
- login
- nom
- prenom
- email
- date_embauche
- type_contrat
```

## Bonnes pratiques

### Sécurité
1. ✅ Changer le mot de passe admin par défaut
2. ✅ Activer l'authentification 2FA
3. ✅ Limiter les tentatives de connexion
4. ✅ Logs d'audit activés
5. ✅ Sauvegardes quotidiennes

### Performance
1. ✅ Nettoyer les logs > 6 mois
2. ✅ Archiver les données > 3 ans
3. ✅ Optimiser la base de données (ANALYZE)
4. ✅ Mettre en cache les données statiques

### Maintenance
1. **Hebdomadaire:**
   - Vérifier les logs d'erreurs
   - Contrôler l'espace disque

2. **Mensuel:**
   - Mettre à jour Dolibarr
   - Sauvegarder la base
   - Tester la restauration

3. **Annuel:**
   - Audit de sécurité
   - Revue des permissions
   - Formation utilisateurs

## Dépannage

### Problème: Emails non envoyés

**Solution:**
```bash
# Vérifier la configuration SMTP
Logs > Emails > Vérifier erreurs

# Tester manuellement
telnet smtp.office365.com 587
```

### Problème: Calcul congés incorrect

**Solution:**
```
1. Vérifier solde initial employé
2. Contrôler les compteurs
3. Recalculer les soldes:
   RH > Congés > Outils > Recalcul
```

## Support

**Documentation:** https://wiki.dolibarr.org  
**Forum:** https://www.dolibarr.fr/forum  
**Tickets:** support@entreprise.fr

---
**Version:** 1.0  
**Dernière MAJ:** Décembre 2025  
**Auteur:** Ahmed Ayadi - Stage QA
