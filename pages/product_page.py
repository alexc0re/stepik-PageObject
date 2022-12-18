from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):


    def add_to_cart(self):
        assert True




    def find_and_click_btn(self):
        self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN)
        self.click_on_elem(*ProductPageLocators.ADD_TO_BASKET_BTN)





    def get_success_message_text(self):
        item_message = self.get_text(*ProductPageLocators.SUCCESS_MESSAGE_ITEM)
        item_price_message = self.get_text(*ProductPageLocators.SUCCESS_MESSAGE_PRICE)
        return item_message, item_price_message



    def check_adding_to_basket(self):
        item_name = self.get_text(*ProductPageLocators.ITEM_NAME)
        item_msg = self.get_text(*ProductPageLocators.SUCCESS_MESSAGE_ITEM)
        item_price = self.get_text(*ProductPageLocators.ITEM_PRICE)
        price_msg = self.get_text(*ProductPageLocators.SUCCESS_MESSAGE_PRICE)

        assert item_name == item_msg, f'{item_name} is not in : {item_msg}'
        assert item_price in price_msg, f'{item_name} is not in : {item_msg}'