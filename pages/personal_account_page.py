from selenium.webdriver.common.by import By
from config import ACCOUNT_URL

class PersonalAccountPage:
    URL = ACCOUNT_URL

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка ЛК
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выход"