from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registration_page import RegistrationPage
from utils.generators import generate_email, generate_password, generate_invalid_email

def test_name_should_not_be_empty():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(RegistrationPage.URL)
    WebDriverWait(driver, 20).until(EC.url_contains("register"))
    driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(generate_password())
    driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()
    error_text = driver.find_element(*RegistrationPage.ERROR_MESSAGE).text
    assert "Поле не может быть пустым" in error_text
    driver.quit()

def test_email_should_be_valid_format():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(RegistrationPage.URL)
    WebDriverWait(driver, 10).until(EC.url_contains("register"))
    driver.find_element(*RegistrationPage.NAME_INPUT).send_keys("Тестовый Пользователь")
    driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(generate_invalid_email())
    driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(generate_password())
    driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()
    error_text = driver.find_element(*RegistrationPage.ERROR_MESSAGE).text
    assert "Введите корректный email" in error_text
    driver.quit()

def test_password_should_be_minimum_6_chars():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(RegistrationPage.URL)
    WebDriverWait(driver, 10).until(EC.url_contains("register"))
    driver.find_element(*RegistrationPage.NAME_INPUT).send_keys("Тестовый Пользователь")
    driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys("12345")
    driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()
    error_text = driver.find_element(*RegistrationPage.ERROR_MESSAGE).text
    assert "Некорректный пароль" in error_text
    driver.quit()

def test_successful_registration():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(RegistrationPage.URL)
    WebDriverWait(driver, 10).until(EC.url_contains("register"))
    driver.find_element(*RegistrationPage.NAME_INPUT).send_keys("Тестовый Пользователь")
    email = generate_email()
    password = generate_password()
    driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_contains("login"))
    assert "login" in driver.current_url
    driver.quit()