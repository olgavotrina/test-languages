from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn[href$='basket/']")


class BasketPageLocators():
    BASKET_ITEMS_AREA = (By.CSS_SELECTOR, ".basket - items")
    EMPTY_BASKET_MSG = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class MainPageLocators():
    pass


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form.add-to-basket")
    ALERT_ITEM_ADDED = (By.CSS_SELECTOR, ".alert-success")
    ALERT_ABOUT_BASKET_SUM = (By.CSS_SELECTOR, ".alert-info")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")


