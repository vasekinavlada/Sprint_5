from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.constructor_page import ConstructorPage

def test_switch_to_buns_tab():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ConstructorPage.BUNS_TAB)).click()
    assert "Булки" in driver.find_element(*ConstructorPage.ACTIVE_TAB).text
    driver.quit()

def test_switch_to_sauces_tab():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ConstructorPage.SAUCES_TAB)).click()
    assert "Соусы" in driver.find_element(*ConstructorPage.ACTIVE_TAB).text
    driver.quit()

def test_switch_to_fillings_tab():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ConstructorPage.FILLINGS_TAB)).click()
    assert "Начинки" in driver.find_element(*ConstructorPage.ACTIVE_TAB).text
    driver.quit()

def test_go_to_constructor_from_logo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/account")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ConstructorPage.LOGO)).click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
    driver.quit()

def test_go_to_constructor_from_link():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/account")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ConstructorPage.CONSTRUCTOR_LINK)).click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
    driver.quit()