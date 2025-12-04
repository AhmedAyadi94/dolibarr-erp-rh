# Tests et Assurance Qualité (QA)

## Vue d'ensemble

Ce document décrit la stratégie de tests et les procédures d'assurance qualité pour le projet Dolibarr ERP RH de TELCO GROUP. Il définit les méthodologies, les scénarios de test, et les critères d'acceptation pour garantir la qualité et la fiabilité du système.

## Objectifs QA

### Objectifs Principaux

1. **Qualité Fonctionnelle**
   - Vérifier que toutes les fonctionnalités répondent aux spécifications
   - S'assurer de la cohérence des données
   - Valider les workflows métier

2. **Performance et Fiabilité**
   - Temps de réponse < 2 secondes pour les opérations courantes
   - Disponibilité système > 99%
   - Support de 100 utilisateurs concurrents

3. **Sécurité**
   - Protection des données personnelles (RGPD)
   - Contrôle d'accès et authentification
   - Audit des accès aux données sensibles

4. **Compatibilité**
   - Navigateurs : Chrome, Firefox, Edge (3 dernières versions)
   - Résolutions : 1366x768 minimum
   - Mobile-responsive pour consultation

### Indicateurs de Qualité

- **Couverture de tests** : > 80% du code
- **Taux de réussite des tests** : > 95%
- **Défaut critique avant production** : 0
- **Défaut majeur avant production** : < 5

## Stratégie de Tests

### Approche Globale

Nous adoptons une approche de tests hybride combinant :
- **Tests manuels** pour les scénarios métier complexes
- **Tests automatisés** pour les régressions et les tests répétitifs
- **Tests exploratoires** pour identifier les cas limites

### Types de Tests

#### 1. Tests Unitaires

**Objectif** : Vérifier les fonctions individuelles
**Outils** : pytest, unittest
**Couverture** : Fonctions de calcul, validations

#### 2. Tests d'Intégration

**Objectif** : Vérifier l'interaction entre modules
**Outils** : pytest, Selenium
**Focus** : Flux de données entre modules RH

#### 3. Tests Fonctionnels

**Objectif** : Valider les fonctionnalités métier
**Outils** : Selenium, Playwright
**Couverture** : Tous les modules RH

#### 4. Tests de Régression

**Objectif** : S'assurer qu'aucune régression n'est introduite
**Fréquence** : À chaque mise à jour
**Automatisation** : 100%

#### 5. Tests de Performance

**Objectif** : Vérifier temps de réponse et charge
**Outils** : JMeter, Locust
**Scénarios** : 100 utilisateurs concurrents

## Environnements de Test

### 1. Environnement de Développement (DEV)

```
URL: http://dev.erp-telco.local
Base de données: dolibarr_dev
Utilisateurs: Développeurs
Données: Jeu de test minimal
```

### 2. Environnement de Test (QA)

```
URL: http://qa.erp-telco.local
Base de données: dolibarr_qa
Utilisateurs: Testeurs QA
Données: Jeu de données complet anonymisé
```

### 3. Environnement de Préproduction (UAT)

```
URL: http://uat.erp-telco.local
Base de données: dolibarr_uat
Utilisateurs: Utilisateurs finaux
Données: Copie production anonymisée
```

## Scénarios de Test

### Module Employés

#### TC-EMP-001 : Création Employé

**Précondition** : Utilisateur connecté avec droits RH

**Étapes** :
1. Naviguer vers RH > Employés > Nouveau
2. Saisir : Nom, Prénom, Email
3. Sélectionner : Poste, Département
4. Définir : Date d'entrée, Salaire
5. Cliquer "Enregistrer"

**Résultat attendu** :
- Employé créé avec ID unique
- Fiche visible dans liste
- Email notification envoyé

**Données de test** :
```
Nom: Dupont
Prénom: Jean
Email: jean.dupont@telcogroup.fr
Poste: Technicien Fibre
Département: Technique
```

### Module Congés

#### TC-CONG-001 : Demande Congés Payés

**Précondition** : Employé connecté avec solde CP > 0

**Étapes** :
1. Accéder Congés > Nouvelle demande
2. Sélectionner type : Congés payés
3. Définir : Date début, Date fin
4. Ajouter commentaire (optionnel)
5. Soumettre demande

**Résultat attendu** :
- Demande créée avec statut "En attente"
- Notification envoyée au manager
- Solde prévisionnel mis à jour

## Outils et Frameworks

### Automatisation Tests

**Selenium WebDriver**
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://qa.erp-telco.local")
```

**Pytest**
```python
import pytest

def test_employee_creation():
    # Test implementation
    assert True
```

### Gestion Tests

- **TestRail** : Gestion cas de test
- **Jira** : Suivi bugs et anomalies
- **GitHub Actions** : CI/CD intégration

## Procédure de Test

### Avant Chaque Release

1. **Exécution suite tests automatiques**
   - Durée : ~2 heures
   - Taux succès requis : > 95%

2. **Tests manuels critiques**
   - Scénarios priorité haute
   - Vérification UI/UX

3. **Tests de régression**
   - Toutes fonctionnalités existantes
   - Focus sur modules modifiés

4. **Tests de performance**
   - Test charge 100 utilisateurs
   - Vérification temps de réponse

5. **Tests de sécurité**
   - Scan vulnérabilités
   - Vérification droits d'accès

### Checklist Go/No-Go

- [ ] Tous tests automatiques passés
- [ ] 0 bug critique
- [ ] < 5 bugs majeurs
- [ ] Tests performance OK
- [ ] Tests sécurité OK
- [ ] Documentation à jour
- [ ] Formation utilisateurs effectuée
- [ ] Plan de rollback prêt

## Rapport de Bugs

### Template Bug Report

**ID**: BUG-XXX
**Sévérité**: Critique/Majeur/Mineur
**Module**: [Nom du module]
**Version**: [Numéro version]

**Description**:
[Description claire du problème]

**Étapes de reproduction**:
1. [Etape 1]
2. [Etape 2]
3. [Etape 3]

**Résultat attendu**:
[Ce qui devrait se passer]

**Résultat obtenu**:
[Ce qui se passe réellement]

**Environnement**:
- OS: [Windows/Linux/Mac]
- Navigateur: [Chrome/Firefox/Edge + version]
- URL: [URL de l'environnement]

**Captures d'écran**:
[Joindre captures si applicable]

### Niveaux de Sévérité

**Critique** : Bloquant, empêche utilisation
- Perte de données
- Application inaccessible
- Faille de sécurité majeure

**Majeur** : Impact important
- Fonctionnalité principale non fonctionnelle
- Contournement possible mais complexe
- Performance dégradée

**Mineur** : Impact limité
- Problème cosmétique
- Contournement facile
- Fonctionnalité secondaire

## Scripts de Test

Voir répertoire `tests/` pour les scripts d'automatisation :
- `test_employes.py` : Tests module employés
- `test_conges.py` : Tests module congés
- `test_paie.py` : Tests module paie
- `test_notes_frais.py` : Tests notes de frais

## Contact Équipe QA

**Responsable QA** : Ahmed Ayadi
**Email** : ahmed.ayadi@telcogroup.fr
**Slack** : #qa-dolibarr

---

**Dernière mise à jour** : 04/12/2025
**Version document** : 1.0
**Auteur** : Ahmed Ayadi - QA Engineer
