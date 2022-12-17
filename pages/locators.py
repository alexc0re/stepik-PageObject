from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "[name=login_submit]")
    REGISTRATION_FORM = (By.CSS_SELECTOR, ".register_form")
