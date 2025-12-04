# Modules RH Dolibarr

## Vue d'ensemble

Ce document décrit les principaux modules de Ressources Humaines activés et configurés dans l'installation Dolibarr ERP pour la gestion RH de TELCO GROUP.

## Modules RH Actifs

### 1. Module Ressources Humaines (Core)

Le module principal de gestion des ressources humaines.

**Fonctionnalités principales :**
- Gestion des fiches employés
- Suivi des informations personnelles
- Gestion des contrats de travail
- Historique des postes et départements
- Documents RH attachés (contrats, avenants, etc.)

**Activation :**
```
Configuration → Modules → Ressources Humaines → Activer
```

**Permissions :**
- Administrateur RH : Tous les droits
- Manager : Lecture et modification équipe
- Employé : Lecture propre fiche uniquement

### 2. Module Congés et Absences

Gestion complète des demandes de congés et absences.

**Fonctionnalités :**
- Demandes de congés (payés, RTT, sans solde)
- Validation hiérarchique des demandes
- Calcul automatique des soldes
- Calendrier des absences
- Reporting et statistiques

**Types de congés configurés :**
- Congés payés (CP)
- Réduction du Temps de Travail (RTT)
- Congés sans solde
- Congés maladie
- Congés exceptionnels (mariage, naissance, décès)

**Workflow de validation :**
1. Employé : Création de la demande
2. Manager direct : Validation niveau 1
3. RH : Validation niveau 2 (finale)
4. Notification automatique par email

### 3. Module Paie et Salaires

Gestion de la paie et des éléments de rémunération.

**Fonctionnalités :**
- Création des fiches de paie
- Gestion des éléments de salaire (fixe, variable, primes)
- Calcul des charges sociales
- Historique des rémunérations
- Export vers logiciel de paie externe

**Éléments de paie :**
- Salaire de base
- Primes (performance, ancienneté, déplacement)
- Heures supplémentaires
- Indemnités (transport, repas)
- Retenues (absences, avances)

**Export :**
Compatible avec les formats :
- CSV pour import Excel
- Format SAGE
- Format CEGID

### 4. Module Notes de Frais

Gestion des frais professionnels engagés par les employés.

**Fonctionnalités :**
- Saisie des notes de frais
- Attachement des justificatifs (tickets, factures)
- Circuit de validation
- Remboursement et export comptable

**Types de frais :**
- Frais kilométriques
- Repas
- Hébergement
- Transport
- Fournitures
- Autres frais professionnels

**Barème kilométrique :**
Utilisation du barème fiscal français en vigueur.

### 5. Module Temps et Activités

Suivi du temps de travail et des activités projet.

**Fonctionnalités :**
- Saisie des temps (timesheet)
- Imputation sur projets et tâches
- Suivi des heures travaillées
- Calcul heures supplémentaires
- Reporting temps par projet/employé

**Modes de saisie :**
- Saisie manuelle quotidienne
- Saisie hebdomadaire
- Import depuis feuille Excel

### 6. Module Recrutement

Gestion du processus de recrutement (module tiers).

**Fonctionnalités :**
- Gestion des offres d'emploi
- Suivi des candidatures
- Évaluation des candidats
- Historique des entretiens
- Intégration nouvel employé

**Workflow :**
1. Création offre d'emploi
2. Réception candidatures
3. Présélection CV
4. Entretiens RH
5. Entretiens techniques
6. Décision finale
7. Onboarding

### 7. Module Formation

Gestion du plan de formation (module tiers).

**Fonctionnalités :**
- Catalogue de formations
- Demandes de formation
- Planification sessions
- Suivi des participants
- Évaluation post-formation
- Budget formation

## Configuration Spécifique TELCO GROUP

### Organigramme

Structure hiérarchique configurée :
```
Directeur Général
├── Directeur Technique
│   ├── Conducteurs de Travaux
│   └── Techniciens
├── Directeur Commercial
│   └── Équipe Commerciale
└── Services Support
    ├── GRH
    ├── Comptabilité
    └── Administratif
```

### Droits d'Accès

**Profils configurés :**

1. **Administrateur Système**
   - Accès complet tous modules
   - Configuration système
   - Gestion utilisateurs

2. **Directeur Général**
   - Vue globale tous employés
   - Validation congés niveau final
   - Accès reporting RH

3. **Responsable RH**
   - Gestion complète employés
   - Validation congés et notes de frais
   - Gestion paie et formation

4. **Manager/Chef d'Équipe**
   - Vue équipe uniquement
   - Validation congés équipe (niveau 1)
   - Saisie temps équipe

5. **Employé**
   - Vue propre fiche
   - Demande congés
   - Saisie notes de frais et temps

### Paramètres Spécifiques

**Congés :**
- Année comptable : Janvier à Décembre
- Acquisition CP : 2,5 jours/mois
- Report CP : 15 jours maximum
- Délai demande : 48h minimum

**Paie :**
- Périodicité : Mensuelle
- Date limite saisie éléments variables : 25 du mois
- Virement salaires : 30 du mois

**Temps de travail :**
- Horaire standard : 35h/semaine
- Semaine type : Lundi-Vendredi
- Heures supp. : Majoration 25% (8 premières), 50% (suivantes)

## Intégrations

### Modules Complémentaires

- **Module Projet** : Imputation temps sur projets chantiers
- **Module Comptabilité** : Export écritures paie et notes de frais
- **Module Documents** : Stockage documents RH (contrats, CV, etc.)

### API et Exports

- Export masse salariale vers comptabilité
- Import employés depuis fichier CSV
- API REST pour intégration badgeuse (futur)

## Maintenance et Mises à Jour

**Sauvegarde :**
- Base de données : Quotidienne (nuit)
- Documents RH : Quotidienne (nuit)
- Rétention : 90 jours

**Mises à jour :**
- Version Dolibarr : Trimestrielle
- Modules tiers : Selon disponibilité
- Tests : Environnement pré-production

## Support et Documentation

**Ressources :**
- Documentation officielle : https://wiki.dolibarr.org
- Forum communauté : https://www.dolibarr.fr/forum
- Support TELCO GROUP : support.erp@telcogroup.fr

**Guides utilisateurs :**
- Guide employé : `docs/guide-employe.pdf`
- Guide manager : `docs/guide-manager.pdf`
- Guide RH : `docs/guide-rh-admin.pdf`

## Prochaines Évolutions

**Roadmap modules RH :**

**Q1 2025 :**
- Intégration badgeuse automatique
- Application mobile saisie temps
- Signature électronique documents

**Q2 2025 :**
- Module évaluation performance
- Gestion des compétences
- Plan de carrière

**Q3 2025 :**
- Portail RH self-service amélioré
- Chat bot RH questions fréquentes
- Analytics RH avancés

---

**Dernière mise à jour :** 04/12/2025  
**Responsable :** Hatouma - GRH  
**Version Dolibarr :** 18.0.4
