from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Should be message about basket is empty, but it is not"
    

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY), "Shouldn't be products in basket, but basket is not empty"
        