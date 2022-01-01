import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--language", action= "store", default=None, help="Choose language: ") #ƒобавл€ем возможность выбора €зыка через командную строку

@pytest.fixture(scope="function")

def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit() #«акрываем барузер после теста
