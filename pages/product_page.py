from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_item_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def get_attribute_of_elem(self, by, what, attribute):
        elem = self.browser.find_element(by, what)
        return elem.get_attribute(attribute)
