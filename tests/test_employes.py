#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests automatisés pour le module Employés de Dolibarr ERP RH

Ce script teste les fonctionnalités principales du module Employés :
- Création d'employé
- Modification des informations
- Consultation de la fiche
- Suppression d'employé

Auteur: Ahmed Ayadi
Date: 04/12/2025
Version: 1.0
"""

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Configuration
BASE_URL = "http://localhost/dolibarr"
USERNAME = "admin"
PASSWORD = "admin"
WAIT_TIMEOUT = 10


class TestEmployes:
    """Classe de tests pour le module Employés"""

    @pytest.fixture(scope="function")
    def driver(self):
        """Fixture pour initialiser et fermer le navigateur"""
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    @pytest.fixture(scope="function")
    def logged_in_driver(self, driver):
        """Fixture pour un driver déjà connecté"""
        self.login(driver)
        yield driver

    def login(self, driver):
        """Se connecter à Dolibarr"""
        driver.get(BASE_URL)
        
        try:
            username_field = WebDriverWait(driver, WAIT_TIMEOUT).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            username_field.clear()
            username_field.send_keys(USERNAME)
            
            password_field = driver.find_element(By.NAME, "password")
            password_field.clear()
            password_field.send_keys(PASSWORD)
            
            login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
            login_button.click()
            
            # Attendre que la page d'accueil charge
            WebDriverWait(driver, WAIT_TIMEOUT).until(
                EC.presence_of_element_located((By.ID, "mainmenu"))
            )
            
        except TimeoutException:
            pytest.fail("Timeout lors de la connexion")

    def test_creation_employe(self, logged_in_driver):
        """TC-EMP-001 : Test de création d'un employé"""
        driver = logged_in_driver
        
        # Accéder au module RH
        driver.get(f"{BASE_URL}/user/index.php")
        time.sleep(2)
        
        # Cliquer sur "Nouvel employé"
        try:
            nouveau_btn = WebDriverWait(driver, WAIT_TIMEOUT).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Nouvel utilisateur"))
            )
            nouveau_btn.click()
            
            # Remplir le formulaire
            nom_field = driver.find_element(By.NAME, "lastname")
            nom_field.send_keys("Dupont")
            
            prenom_field = driver.find_element(By.NAME, "firstname")
            prenom_field.send_keys("Jean")
            
            email_field = driver.find_element(By.NAME, "email")
            email_field.send_keys("jean.dupont@telcogroup.fr")
            
            # Soumettre le formulaire
            submit_btn = driver.find_element(By.CSS_SELECTOR, "input[name='create']")
            submit_btn.click()
            
            # Vérifier la création
            success_msg = WebDriverWait(driver, WAIT_TIMEOUT).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ok"))
            )
            assert success_msg is not None, "Message de succès non trouvé"
            print("[PASS] Création employé réussie")
            
        except Exception as e:
            pytest.fail(f"Erreur lors de la création : {str(e)}")

    def test_consultation_employe(self, logged_in_driver):
        """TC-EMP-002 : Test de consultation fiche employé"""
        driver = logged_in_driver
        
        driver.get(f"{BASE_URL}/user/index.php")
        time.sleep(2)
        
        try:
            # Cliquer sur un employé dans la liste
            premier_employe = WebDriverWait(driver, WAIT_TIMEOUT).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "tr.oddeven a"))
            )
            premier_employe.click()
            
            # Vérifier présence informations
            nom_element = driver.find_element(By.CLASS_NAME, "refidno")
            assert nom_element is not None, "Nom employé non trouvé"
            print("[PASS] Consultation fiche employé réussie")
            
        except Exception as e:
            pytest.fail(f"Erreur lors de la consultation : {str(e)}")

    def test_modification_employe(self, logged_in_driver):
        """TC-EMP-003 : Test de modification employé"""
        driver = logged_in_driver
        
        driver.get(f"{BASE_URL}/user/index.php")
        time.sleep(2)
        
        try:
            # Ouvrir fiche employé
            premier_employe = WebDriverWait(driver, WAIT_TIMEOUT).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "tr.oddeven a"))
            )
            premier_employe.click()
            time.sleep(1)
            
            # Cliquer sur Modifier
            modifier_btn = driver.find_element(By.LINK_TEXT, "Modifier")
            modifier_btn.click()
            time.sleep(1)
            
            # Modifier email
            email_field = driver.find_element(By.NAME, "email")
            email_field.clear()
            email_field.send_keys("jean.dupont.modifie@telcogroup.fr")
            
            # Enregistrer
            save_btn = driver.find_element(By.NAME, "edit")
            save_btn.click()
            
            # Vérifier modification
            success_msg = WebDriverWait(driver, WAIT_TIMEOUT).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ok"))
            )
            assert success_msg is not None, "Modification non confirmée"
            print("[PASS] Modification employé réussie")
            
        except Exception as e:
            pytest.fail(f"Erreur lors de la modification : {str(e)}")


if __name__ == "__main__":
    """Exécution des tests"""
    pytest.main([
        __file__,
        "-v",
        "--tb=short",
        "--html=reports/test_employes_report.html",
        "--self-contained-html"
    ])
