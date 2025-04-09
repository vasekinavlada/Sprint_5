import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locator import LoginLocator
from config import BASE_URL, HOME_URL, LOGIN_URL, REGISTER_URL, ACCOUNT_URL


# 1. Вход по кнопке «Войти в аккаунт» на главной
def test_login_via_main_page_button(driver, register_user):
    driver.get(HOME_URL)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginLocator.LOGIN_BUTTON)
    ).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginLocator.EMAIL_INPUT)
    ).send_keys(register_user["email"])

    driver.find_element(*LoginLocator.PASSWORD_INPUT).send_keys(register_user["password"])
    driver.find_element(*LoginLocator.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be(ACCOUNT_URL)
    )

    assert driver.current_url == ACCOUNT_URL, \
        f"Ожидался переход на {ACCOUNT_URL}, получен {driver.current_url}"


# 2. Вход через кнопку «Личный кабинет»
def test_login_via_profile_button(driver, register_user):

    driver.get(HOME_URL)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginLocator.PROFILE_BUTTON)
    ).click()
    WebDriverWait(driver, 10).until(
        EC.url_to_be(LOGIN_URL)
    )

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginLocator.EMAIL_INPUT)
    ).send_keys(register_user["email"])

    driver.find_element(*LoginLocator.PASSWORD_INPUT).send_keys(register_user["password"])
    driver.find_element(*LoginLocator.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be(ACCOUNT_URL)
    )
    assert driver.current_url == ACCOUNT_URL, \
        f"Ожидался переход на {ACCOUNT_URL}, получен {driver.current_url}"


# 3. Вход через кнопку в форме регистрации
def test_login_via_register_page(driver, register_user):
    driver.get(REGISTER_URL)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginLocator.LOGIN_LINK_ON_REGISTER)
    ).click()
    WebDriverWait(driver, 10).until(
        EC.url_to_be(LOGIN_URL)
    )

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginLocator.EMAIL_INPUT)
    ).send_keys(register_user["email"])

    driver.find_element(*LoginLocator.PASSWORD_INPUT).send_keys(register_user["password"])
    driver.find_element(*LoginLocator.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be(ACCOUNT_URL)
    )
    assert driver.current_url == ACCOUNT_URL, \
        f"Ожидался переход на {ACCOUNT_URL}, получен {driver.current_url}"


# 4. Вход через форму восстановления пароля
def test_login_via_forgot_password_page(driver, register_user):
    driver.get(f"{BASE_URL}/forgot-password")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginLocator.LOGIN_LINK_ON_FORGOT_PASSWORD)
    ).click()
    WebDriverWait(driver, 10).until(
        EC.url_to_be(LOGIN_URL)
    )

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginLocator.EMAIL_INPUT)
    ).send_keys(register_user["email"])

    driver.find_element(*LoginLocator.PASSWORD_INPUT).send_keys(register_user["password"])
    driver.find_element(*LoginLocator.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be(ACCOUNT_URL)
    )
    assert driver.current_url == ACCOUNT_URL, \
        f"Ожидался переход на {ACCOUNT_URL}, получен {driver.current_url}"

