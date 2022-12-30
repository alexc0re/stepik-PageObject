from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
from pages.locators import LoginPageLocators
from pages.locators import BasketPageLocators
from pages.base_page import BasePage
from pages.login_page import LoginPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)







