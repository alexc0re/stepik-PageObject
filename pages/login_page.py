from .base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.is_element_present(*LoginPageLocators.LOGIN_LINK)
        assert 'login' in self.driver.current_url

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTRATION_FORM)
        assert True

    def register_new_user(self, email, password):
        self.driver.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.driver.find_element(*LoginPageLocators.REGISTRATION_PASS1).send_keys(password)
        self.driver.find_element(*LoginPageLocators.REGISTRATION_PASS2).send_keys(password)
        self.driver.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()