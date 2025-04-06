from selenium.webdriver.common.by import By
from config import LOGIN_URL

class LoginPage:
    URL = LOGIN_URL

    EMAIL_INPUT = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")  # Поле Email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле Пароль
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа