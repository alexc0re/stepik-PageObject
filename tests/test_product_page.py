import time
import pytest
from pages.product_page import ProductPage
from pages.base_page import BasePage


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                               "/?promo=offer7", marks=pytest.mark.xfail),

                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(driver, link):
    page = ProductPage(driver,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.find_and_click_btn()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.check_adding_to_basket()



def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
    page = ProductPage(driver, link)
    page.open()
    page.find_and_click_btn()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(driver):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
    page = ProductPage(driver, link)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(driver):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
    page = ProductPage(driver, link)
    page.open()
    page.find_and_click_btn()
    page.should_be_dissapeares()

def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(driver, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    base_page = BasePage(driver, link)
    product_page = ProductPage(driver, link)
    base_page.open()
    base_page.should_be_login_link()
    product_page.find_and_click_login_button()
