from pages.main_page import MainPage
from pages.base_page import BasePage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open_link()                      # открываем страницу
    page.go_to_login_page()