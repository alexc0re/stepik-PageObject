from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
from pages.locators import LoginPageLocators
from pages.locators import BasketPageLocators
from pages.base_page import BasePage
from pages.login_page import LoginPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


    def go_to_login_page(self):
        login_link = self.driver.find_element(*LoginPageLocators.LOGIN_LINK)
        login_link.click()
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass
        return LoginPage(driver=self.driver, url=self.driver.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"






