from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    #селекторы для получения данных из товара
    PRODUCT = (By.CSS_SELECTOR, "h1")
    COST_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    #селекторы для получения данных из алертов
    PRODUCT_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    TOTAL_BASKET = (By.CSS_SELECTOR, ".alert-info>div>p strong")