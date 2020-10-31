from selenium.webdriver.chrome.options import Options

import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language for testing")

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser..")

    #считывание языка из командной строки
    lang_browser = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang_browser})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
