import pytest
from selenium import webdriver

@pytest.fixture
def open_kinopoisk():
    driver = webdriver.Firefox()
    driver.get('https://www.kinopoisk.ru/')
    yield driver
    driver.quit()

