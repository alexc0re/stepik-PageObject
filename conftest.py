import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from webdriver_manager.microsoft import EdgeChromiumDriverManager




chrome_options = ChromeOptions()
edge_options = webdriver.EdgeOptions()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")  # browser selection

    parser.addoption('--language', action='store', default='en',  # Browser Language selection
                     help="Choose language: en or es")

    parser.addoption('--browser_mode', action='store', default='start-maximized',  # Browser mode selection
                     help="--headless mode")




@pytest.fixture(scope="session")
def driver(request):
    driver_mode = request.config.getoption('browser_mode')
    driver_lang = request.config.getoption("language")
    driver_name = request.config.getoption('browser_name')

    driver = None
    if driver_name == 'chrome':
        chrome_options.add_argument(driver_mode)
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': driver_lang})
        print(f"\nstart {driver_lang}  {driver_name} chrome browser with {driver_mode} parameter")
        print("Start chrome browser for tests")
        driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))

    elif driver == 'remote':
        driver = webdriver.Remote(
            command_executor="http://selenium-hub.ss.svc.cluster.local:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, "CHROME"))

    elif driver_name == 'edge':
        print(f"\nstart {driver_lang}  {driver_name} chrome browser with {driver_mode} parameter")
        edge_options.add_argument("--mute-audio")
        edge_options.add_argument(driver_mode)
        driver = webdriver.Edge((EdgeChromiumDriverManager().install()), options=edge_options)

    yield driver
    print("\nquit browser..")
    driver.quit()