import time
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.locators import MainPageLocators


def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина



def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/'
    base_page = BasePage(driver, link)
    main_page = MainPage(driver, link)
    basket_page = BasketPage(driver, link)
    base_page.open()
    basket_page.go_to_basket()
    time.sleep(5)
    assert 1 == 1