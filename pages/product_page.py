from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()
        #self.solve_quiz_and_get_code()
        
    def should_be_message_about_adding_product_to_basket(self, product_name):
        message_adding = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_MESSAGE)
        assert message_adding.text == product_name, "Name in message not equal name product"


    def should_be_sum_in_basket_equal_price_of_product(self, cost_prod):
        total_basket = self.browser.find_element(*ProductPageLocators.TOTAL_BASKET).text
        assert total_basket == cost_prod, "Not equal product price and total sum of basket"
        
    def extract_product_name(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT)
        return product.text

    def extract_product_price(self):
        return self.browser.find_element(*ProductPageLocators.COST_PRODUCT).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_IN_MESSAGE), "Success message is presented, but should not be"

    def should_be_disable_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_IN_MESSAGE), "Success message is not disabled, but it still here"