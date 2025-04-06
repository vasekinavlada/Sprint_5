
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from utils.generators import generate_email, generate_password, generate_invalid_email


# 1. Вход по кнопке «Войти в аккаунт» на главной
def test_login_via_main_page_button():
    driver = webdriver.Chrome()
    try:
        # Тестовые данные
        test_email = generate_email()
        test_password = generate_password()

        # Переход и действия
        driver.get(RegistrationPage.URL)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
        ).click()

        # Заполнение формы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='name']"))
        ).send_keys(test_email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(test_password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        # Проверка
        WebDriverWait(driver, 10).until(
            EC.url_to_be(RegistrationPage.URL)
        )
    finally:
        driver.quit()


# 2. Вход через кнопку «Личный кабинет»
def test_login_via_profile_button():
    driver = webdriver.Chrome()
    try:
        test_email = generate_email()
        test_password = generate_password()

        driver.get(RegistrationPage.URL)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/account']"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='name']"))
        ).send_keys(test_email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(test_password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("account")
        )
    finally:
        driver.quit()


# 3. Вход через кнопку в форме регистрации
def test_login_via_register_page():
    driver = webdriver.Chrome()
    try:
        test_email = "test@example.com"
        test_password = "password123"

        driver.get(RegistrationPage.URL)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Войти']"))
        ).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LoginPage.URL))

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='name']"))
        ).send_keys(test_email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(test_password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    finally:
        driver.quit()

#4. Вход через форму восстановления пароля
def test_login_via_forgot_password_page():
    driver = webdriver.Chrome()
    try:
        test_email = "test@example.com"
        test_password = "password123"

        driver.get(RegistrationPage.URL)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Войти']"))
        ).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(LoginPage.URL))

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='name']"))
        ).send_keys(test_email)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(test_password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    finally:
        driver.quit()