from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
from pages.base_page import BasePage
from pages.login_page import LoginPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def find_and_basket_button(self):
        self.is_element_present(*MainPageLocators.BASKET_BUTTON)
        self.click_on_elem(*MainPageLocators.BASKET_BUTTON)
