from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()
        self.solve_quiz_and_get_code()
        self.should_be_message_about_adding_to_basket()
        self.should_be_sum_equal_price_of_product()

    def should_be_message_about_adding_to_basket(self):
        message_adding = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_MESSAGE)
        product = self.browser.find_element(*ProductPageLocators.PRODUCT)
        name_product = product.text
        assert message_adding.text.find(name_product) != -1, "Not Found message about adding to basket"


    def should_be_sum_equal_price_of_product(self):
        message_total_basket = self.browser.find_element(*ProductPageLocators.TOTAL_BASKET)
        cost_prod = self.browser.find_element(*ProductPageLocators.COST_PRODUCT).text
        assert message_total_basket.text.find(cost_prod)
        
