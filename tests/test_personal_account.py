from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from utils.generators import generate_email, generate_password

def test_go_to_personal_account():
    email = generate_email()
    password = generate_password()

    # Регистрация
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(RegistrationPage.URL)
    WebDriverWait(driver, 10).until(EC.url_contains("register"))
    driver.find_element(*RegistrationPage.NAME_INPUT).send_keys("ЛичныйТест")
    driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()
    driver.quit()

    # Вход
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(LoginPage.URL)
    WebDriverWait(driver, 10).until(EC.url_contains("login"))
    driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()

    # Переход в личный кабинет
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PersonalAccountPage.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.url_contains("account/profile"))
    assert "account/profile" in driver.current_url
    driver.quit()

def test_logout_from_account():
    email = generate_email()
    password = generate_password()

    # Регистрация
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(RegistrationPage.URL)
    WebDriverWait(driver, 10).until(EC.url_contains("register"))
    driver.find_element(*RegistrationPage.NAME_INPUT).send_keys("LogoutTest")
    driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()
    driver.quit()

    # Вход
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(LoginPage.URL)
    WebDriverWait(driver, 10).until(EC.url_contains("login"))
    driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()

    # Выход
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PersonalAccountPage.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PersonalAccountPage.LOGOUT_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.url_contains("login"))
    assert "login" in driver.current_url
    driver.quit()