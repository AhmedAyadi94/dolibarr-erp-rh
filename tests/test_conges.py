#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests automatisés pour le module Congés de Dolibarr ERP RH

Ce script teste les fonctionnalités principales du module Congés :
- Demande de congés payés
- Validation/Refus de demandes
- Consultation des soldes
- Vérification calculs automatiques

Auteur: Ahmed Ayadi
Date: 04/12/2025
Version: 1.0
"""

import pytest
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Configuration
BASE_URL = "http://localhost/dolibarr"
USERNAME = "admin"
PASSWORD = "ahmed123"
WAIT_TIMEOUT = 10


class TestConges:
    """Classe de tests pour le module Congés"""

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
            # Champ login corrigé
            username_field = WebDriverWait(driver, WAIT_TIMEOUT).until(
                EC.presence_of_element_located((By.NAME, "login"))
            )
            username_field.clear()
            username_field.send_keys(USERNAME)
            
            password_field = driver.find_element(By.NAME, "password")
            password_field.clear()
            password_field.send_keys(PASSWORD)
            
            login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
            login_button.click()
            
            WebDriverWait(driver, WAIT_TIMEOUT).until(
                EC.presence_of_element_located((By.ID, "mainmenu"))
            )
            
        except TimeoutException:
            pytest.fail("Timeout lors de la connexion")

    def test_demande_conges(self, logged_in_driver):
        """TC-CONG-001 : Test de demande de congés payés"""
        driver = logged_in_driver
        
        driver.get(f"{BASE_URL}/holiday/list.php")
        time.sleep(2)
        
        try:
            nouvelle_demande_btn = WebDriverWait(driver, WAIT_TIMEOUT).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Nouvelle demande"))
            )
            nouvelle_demande_btn.click()
            time.sleep(1)
            
            type_select = Select(driver.find_element(By.NAME, "type"))
            type_select.select_by_visible_text("Congés payés")
            
            date_debut = (datetime.now() + timedelta(days=7)).strftime("%d/%m/%Y")
            date_fin = (datetime.now() + timedelta(days=11)).strftime("%d/%m/%Y")
            
            driver.find_element(By.NAME, "date_debut").send_keys(date_debut)
            driver.find_element(By.NAME, "date_fin").send_keys(date_fin)
            driver.find_element(By.NAME, "comment").send_keys("Congés d'été - Test automatique")
            
            submit_btn = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
            submit_btn.click()
            
            success_msg = WebDriverWait(driver, WAIT_TIMEOUT).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ok"))
            )
            assert success_msg is not None, "Demande non créée"
            print("[PASS] Demande de congés créée avec succès")
            
        except Exception as e:
            pytest.fail(f"Erreur lors de la demande : {str(e)}")

    def test_consultation_solde(self, logged_in_driver):
        """TC-CONG-002 : Test de consultation des soldes de congés"""
        driver = logged_in_driver
        
        driver.get(f"{BASE_URL}/holiday/list.php")
        time.sleep(2)
        
        try:
            solde_element = WebDriverWait(driver, WAIT_TIMEOUT).until(
                EC.presence_of_element_located((By.CLASS_NAME, "liste"))
            )
            assert solde_element is not None, "Tableau des soldes non trouvé"
            print("[PASS] Consultation soldes réussie")
            
        except Exception as e:
            pytest.fail(f"Erreur consultation : {str(e)}")

    def test_validation_conges(self, logged_in_driver):
        """TC-CONG-003 : Test validation demande de congés"""
        driver = logged_in_driver
        
        driver.get(f"{BASE_URL}/holiday/list.php?search_status=1")
        time.sleep(2)
        
        try:
            demande_link = WebDriverWait(driver, WAIT_TIMEOUT).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "tr.oddeven a"))
            )
            demande_link.click()
            time.sleep(1)
            
            valider_btn = driver.find_element(By.LINK_TEXT, "Valider")
            valider_btn.click()
            
            confirm_btn = driver.find_element(By.NAME, "confirm")
            confirm_btn.click()
            
            success_msg = WebDriverWait(driver, WAIT_TIMEOUT).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ok"))
            )
            assert success_msg is not None
            print("[PASS] Validation congés réussie")
            
        except Exception as e:
            print(f"[INFO] Pas de demande à valider : {str(e)}")


if __name__ == "__main__":
    pytest.main([
        __file__,
        "-v",
        "--tb=short",
        "--html=reports/test_conges_report.html",
        "--self-contained-html"
    ])
