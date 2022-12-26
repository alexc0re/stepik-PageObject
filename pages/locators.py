from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "[name=login_submit]")
    REGISTRATION_FORM = (By.CSS_SELECTOR, ".register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ITEM_NAME = (By.CSS_SELECTOR, '.col-sm-6 h1')
    ITEM_PRICE = (By.CSS_SELECTOR, '.price_color')

    SUCCESS_MESSAGE_ITEM = (By.CSS_SELECTOR, '.alert-success:nth-child(1) .alertinner strong')
    SUCCESS_MESSAGE_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner p ')
