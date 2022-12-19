from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
from pages.base_page import BasePage
from pages.login_page import LoginPage


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except:
            pass
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def test_guest_can_go_to_login_page(self):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(self.browser, link)
        page.open()
        login_page = page.go_to_login_page()
        login_page.should_be_login_page()