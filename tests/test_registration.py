import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.registration_page import RegistrationPage
from utils.generators import generate_email, generate_invalid_email
from config import REGISTER_URL, LOGIN_URL

def test_name_should_not_be_empty(driver, random_user):
    driver.get(REGISTER_URL)
    WebDriverWait(driver, 20).until(EC.url_contains(REGISTER_URL))
    driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(random_user["email"])
    driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(random_user["password"])
    driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()
    error_text = driver.find_element(*RegistrationPage.ERROR_MESSAGE).text
    assert "Поле не может быть пустым" in error_text


def test_email_should_be_valid_format(driver, random_user):
    driver.get(REGISTER_URL)
    WebDriverWait(driver, 10).until(EC.url_contains(REGISTER_URL))
    driver.find_element(*RegistrationPage.NAME_INPUT).send_keys("Тестовый Пользователь")
    driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(generate_invalid_email())
    driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(random_user["password"])
    driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()
    error_text = driver.find_element(*RegistrationPage.ERROR_MESSAGE).text
    assert "Введите корректный email" in error_text


def test_password_should_be_minimum_6_chars(driver, random_user):
    driver.get(REGISTER_URL)
    WebDriverWait(driver, 10).until(EC.url_contains(REGISTER_URL))
    driver.find_element(*RegistrationPage.NAME_INPUT).send_keys("Тестовый Пользователь")
    driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(random_user["email"])
    driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys("12345")
    driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()
    error_text = driver.find_element(*RegistrationPage.ERROR_MESSAGE).text
    assert "Некорректный пароль" in error_text


def test_successful_registration(driver, random_user):
    driver.get(REGISTER_URL)
    WebDriverWait(driver, 10).until(EC.url_contains(REGISTER_URL))
    driver.find_element(*RegistrationPage.NAME_INPUT).send_keys("Тестовый Пользователь")
    driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(random_user["email"])
    driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(random_user["password"])
    driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_contains(LOGIN_URL))
    assert LOGIN_URL in driver.current_url
