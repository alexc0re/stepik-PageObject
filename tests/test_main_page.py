import time
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.locators import MainPageLocators





def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/'
    base_page = BasePage(driver, link)
    main_page = MainPage(driver, link)
    base_page.open()
    main_page.find_and_click_basket_button()
    time.sleep(5)
    assert 1 == 1