import pytest
from selenium.webdriver.common.by import By
import allure

@allure.title("Поиск Фильма по названию")
@allure.severity(allure.severity_level.NORMAL)
def test_search_functionality(driver):
    driver.get('https://www.kinopoisk.ru/')
    driver.find_element(By.NAME, 'kp_query').send_keys('Матрица')
    assert driver.find_element(By.ID, 'suggest-item-film-301').is_displayed()

@allure.title("Поиск фильма по названию")
@allure.description("Ввод названия фильма")
@allure.severity(allure.severity_level.NORMAL)
def test_novipet(driver):
    driver.get('https://www.kinopoisk.ru/')
    driver.find_element(By.NAME, 'kp_query').send_keys('Матрица')
    driver.find_element(By.ID, 'suggest-item-film-301').click()
    assert driver.find_element(By.CSS_SELECTOR, 'span[data-tid="75209b22"]').text=="Матрица (1999)"

@allure.title("Поиск Актера")
@allure.severity(allure.severity_level.NORMAL)
def test_navigate_to_actor(driver):
    driver.get('https://www.kinopoisk.ru/')
    driver.find_element(By.NAME, 'kp_query').send_keys('Брэд Питт')
    assert driver.find_element(By.ID, 'suggest-item-person-25584').is_displayed()

@allure.title("Поиск Актера")
@allure.description("Ввод имени актера")
@allure.severity(allure.severity_level.NORMAL)
def test_get_movie_description(driver):
    driver.get('https://www.kinopoisk.ru/')
    driver.find_element(By.NAME, 'kp_query').send_keys('Брэд Питт')
    driver.find_element(By.ID, 'suggest-item-person-25584').click()
    assert driver.find_element(By.CSS_SELECTOR, 'h1[data-tid="f22e0093"]').text=="Брэд Питт"

@allure.title("Негативная проверка")
@allure.description("Ввод недопустимого значения")
@allure.severity(allure.severity_level.NORMAL)
def test_negative(driver):
    driver.get('https://www.kinopoisk.ru/')
    driver.find_element(By.NAME, 'kp_query').send_keys('135454авяраи№')
    assert driver.find_element(By.XPATH, "//*[contains(@class, 'emptySuggest')]").text == "По вашему запросу ничего не найдено"