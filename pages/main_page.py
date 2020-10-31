from .base_page.py import BasePage
from selenuim.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click() 
    