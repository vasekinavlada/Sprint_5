from selenium.webdriver.common.by import By
from config import REGISTER_URL

class RegistrationPage:
    URL = REGISTER_URL

    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле Имя
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")  # Поле Email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле Пароль
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка регистрации
    ERROR_MESSAGE = (By.CSS_SELECTOR, "p[class*='input__error']")  # Сообщение об ошибке