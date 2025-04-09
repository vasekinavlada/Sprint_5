import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locator import LoginLocator
from config import REGISTER_URL, LOGIN_URL

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def random_user():
    from utils.generators import generate_email
    return {
        "email": generate_email(),
        "password": "qwerty"
    }


@pytest.fixture
def register_user(driver):
    from utils.generators import generate_email

    email = generate_email()
    password = "qwerty"

    driver.get(REGISTER_URL)

    driver.find_element(*LoginLocator.EMAIL_INPUT).send_keys("Test User")
    driver.find_element(*LoginLocator.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginLocator.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginLocator.PROFILE_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be(LOGIN_URL)  # Или ACCOUNT_URL, если сразу редирект на страницу профиля
    )
    return {"email": email, "password": password}