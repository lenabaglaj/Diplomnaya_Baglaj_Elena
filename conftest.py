import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    # Инициализация драйвера
    browser= webdriver.Firefox()
    browser.implicitly_wait(50)
    browser.maximize_window()  # Развернуть окно во весь экран
    yield browser
    # Завершение работы драйвера
    browser.quit()

