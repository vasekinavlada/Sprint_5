from selenium.webdriver.common.by import By

class LoginLocator:

    EMAIL_INPUT = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")  # Поле Email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле Пароль
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа
    PROFILE_BUTTON = (By.XPATH, "//a[@href='/account']") # Кнопка личный кабинет
    LOGIN_LINK_ON_REGISTER = (By.XPATH, "//div[contains(@class, 'Auth_link')]//a[@href='/login' and text()='Войти']") # Для страницы регистрации
    LOGIN_LINK_ON_FORGOT_PASSWORD = (By.XPATH, "//div[contains(@class, 'Auth_form')]//a[@href='/login']") # Для страницы восстановления пароля