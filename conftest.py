import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function') # function - браузер открывается и закрывается после каждого ТЕСТА
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()