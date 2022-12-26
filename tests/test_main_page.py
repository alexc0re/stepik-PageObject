import time

from pages.base_page import BasePage
from pages.locators import MainPageLocators





def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/'
    base_page = BasePage(driver, link)
    main_page = MainPage
    base_page.open()

    base_page.click_on_elem(MainPageLocators.BASKET_BUTTON)
    time.sleep(5)
    assert 1 == 1