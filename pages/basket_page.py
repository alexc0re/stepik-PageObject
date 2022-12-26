from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.locators import BasketPageLocators
class BasketPage(BasePage):


    def go_to_basket(self):
        self.is_element_present(*MainPageLocators.BASKET_BUTTON)
        self.click_on_elem(*MainPageLocators.BASKET_BUTTON)

    def check_is_button_empty(self):
        expected_result = "Your basket is empty"
        actual_result = self.get_text(BasketPageLocators.EMPTY_BASKET)
        assert expected_result == actual_result, f'Failed, expected : {expected_result} but got: {actual_result}'