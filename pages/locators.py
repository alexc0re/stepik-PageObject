from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")



class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn-default:first-child")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "[name=login_submit]")
    REGISTRATION_FORM = (By.CSS_SELECTOR, ".register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "[name=registration-email]")
    REGISTRATION_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".col-sm-6 h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".price_color")
    SUCCESS_MESSAGE_ITEM = (By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner strong")
    SUCCESS_MESSAGE_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner p ")


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg")