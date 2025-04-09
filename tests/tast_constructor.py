import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.constructor_locator import ConstructorLocator
from config import HOME_URL


def test_switch_to_buns_tab(driver):
    driver.get(HOME_URL)
    (WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(ConstructorLocator.BUNS_TAB))
     .click())
    assert "Булки" in driver.find_element(*ConstructorLocator.ACTIVE_TAB).text



def test_switch_to_sauces_tab(driver):
    driver.get(HOME_URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ConstructorLocator.SAUCES_TAB)).click()
    assert "Соусы" in driver.find_element(*ConstructorLocator.ACTIVE_TAB).text


def test_switch_to_fillings_tab(driver):
    driver.get(HOME_URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ConstructorLocator.FILLINGS_TAB)).click()
    assert "Начинки" in driver.find_element(*ConstructorLocator.ACTIVE_TAB).text


def test_go_to_constructor_from_logo(driver):
    driver.get(HOME_URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ConstructorLocator.LOGO)).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(HOME_URL))
    assert driver.current_url == HOME_URL


def test_go_to_constructor_from_link(driver):
    driver.get(HOME_URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ConstructorLocator.CONSTRUCTOR_LINK)).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(HOME_URL))
    assert driver.current_url == HOME_URL
