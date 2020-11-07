from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert url.find("login") != -1, "Adress URL is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"


    def register_new_user(self, email, password):
        time.sleep(5)
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password.send_keys(password)
        registration_btn = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_btn.click()