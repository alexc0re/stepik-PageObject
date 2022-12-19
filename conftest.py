import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as chrome_options

options = Options()


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',  ## Browser Language selection
                     help="Choose language: en or es")


    parser.addoption('--browsermode', action='store', default='start-maximized', ## Browser mode selection
                     help="--headless mode")


@pytest.fixture(scope="session")
def browser(request):
    browser_mode = request.config.getoption('browsermode')
    browser_lang = request.config.getoption("language")
    browser = None
    if browser_lang:
        print("\nstart ES chrome browser for test..")
        options.add_argument(browser_mode)
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
        browser = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))



    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
