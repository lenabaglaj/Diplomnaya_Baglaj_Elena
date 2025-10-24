import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.title("Поиск фильма по названию")
@allure.severity(allure.severity_level.NORMAL)
def test_search_functionality(open_kinopoisk):
    driver = open_kinopoisk
    driver.find_element(By.NAME, 'kp_query').send_keys('Матрица')

    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'suggest-item-film-301'))
    )

    assert element.is_displayed()


@allure.title("Поиск фильма по названию")
@allure.description("Ввод названия фильма")
@allure.severity(allure.severity_level.NORMAL)
def test_novipet(open_kinopoisk):
    driver = open_kinopoisk
    driver.find_element(By.NAME, 'kp_query').send_keys('Матрица')

    suggestion = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'suggest-item-film-301'))
    )
    suggestion.click()

    title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[data-tid="75209b22"]'))
    )

    assert title.text == "Матрица (1999)"


@allure.title("Поиск Актера")
@allure.severity(allure.severity_level.NORMAL)
def test_navigate_to_actor(open_kinopoisk):
    driver = open_kinopoisk
    driver.find_element(By.NAME, 'kp_query').send_keys('Брэд Питт')

    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'suggest-item-person-25584'))
    )

    assert element.is_displayed()


@allure.title("Поиск Актера")
@allure.description("Ввод имени актера")
@allure.severity(allure.severity_level.NORMAL)
def test_get_movie_description(open_kinopoisk):
    driver = open_kinopoisk

    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'kp_query'))
    )

    search_box.send_keys('Брэд Питт')

    actor_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'suggest-item-person-25584'))
    )
    actor_element.click()

    title_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1[data-tid="f22e0093"]'))
    )

    assert title_element.text == "Брэд Питт", f"Expected 'Брэд Питт', but got '{title_element.text}'"


@allure.title("Негативная проверка")
@allure.description("Ввод недопустимого значения")
@allure.severity(allure.severity_level.NORMAL)
def test_negative(open_kinopoisk):
    driver = open_kinopoisk

    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'kp_query'))
    )

    search_box.send_keys('135454авяраи№')

    empty_suggest_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'emptySuggest')]"))
    )

    assert empty_suggest_element.text == "По вашему запросу ничего не найдено", f"Expected 'По вашему запросу ничего не найдено', but got '{empty_suggest_element.text}'"