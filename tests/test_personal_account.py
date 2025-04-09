import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.registration_page import RegistrationPage
from locators.login_locator import LoginLocator
from pages.personal_account_page import PersonalAccountPage
from config import LOGIN_URL, REGISTER_URL, ACCOUNT_URL


def test_go_to_personal_account(driver, random_user):
    # Регистрация
    driver.get(REGISTER_URL)
    WebDriverWait(driver, 10).until(EC.url_contains(REGISTER_URL))
    driver.find_element(*RegistrationPage.NAME_INPUT).send_keys("ЛичныйТест")
    driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(random_user["email"])
    driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(random_user["password"])
    driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()


    # Вход
    driver.get(LOGIN_URL)
    WebDriverWait(driver, 10).until(EC.url_contains(LOGIN_URL))
    driver.find_element(*LoginLocator.EMAIL_INPUT).send_keys(random_user["email"])
    driver.find_element(*LoginLocator.PASSWORD_INPUT).send_keys(random_user["password"])
    driver.find_element(*LoginLocator.LOGIN_BUTTON).click()

    # Переход в личный кабинет
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(PersonalAccountPage.PERSONAL_ACCOUNT_BUTTON)
    ).click()
    WebDriverWait(driver, 10).until(EC.url_contains(ACCOUNT_URL))
    assert ACCOUNT_URL in driver.current_url


def test_logout_from_account(driver, random_user):
    # Регистрация
    driver.get(REGISTER_URL)
    WebDriverWait(driver, 10).until(EC.url_contains(REGISTER_URL))
    driver.find_element(*RegistrationPage.NAME_INPUT).send_keys("LogoutTest")
    driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(random_user["email"])
    driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(random_user["password"])
    driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()

    # Вход
    driver.get(LOGIN_URL)
    WebDriverWait(driver, 10).until(EC.url_contains(LOGIN_URL))
    driver.find_element(*LoginLocator.EMAIL_INPUT).send_keys(random_user["email"])
    driver.find_element(*LoginLocator.PASSWORD_INPUT).send_keys(random_user["password"])
    driver.find_element(*LoginLocator.LOGIN_BUTTON).click()

    # Выход
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(PersonalAccountPage.PERSONAL_ACCOUNT_BUTTON)
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(PersonalAccountPage.LOGOUT_BUTTON)
    ).click()
    WebDriverWait(driver, 10).until(
        EC.url_contains(LOGIN_URL))
    assert LOGIN_URL in driver.current_url
