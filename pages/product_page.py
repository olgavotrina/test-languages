from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_item_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def get_attribute_of_elem(self, by, what, attribute):
        elem = self.browser.find_element(by, what)
        return elem.get_attribute(attribute)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_ITEM_ADDED), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_ITEM_ADDED), \
            "Success message is presented, but should not be"

    def should_be_success_added_item_msg(self):
        success_alert_text = self.get_attribute_of_elem(*ProductPageLocators.ALERT_ITEM_ADDED, "innerText")
        item_name = self.get_attribute_of_elem(*ProductPageLocators.ITEM_NAME, "textContent")
        assert f'{item_name} has been added to your basket' in success_alert_text, "Wrong book name in alert"

    def should_be_correct_price_msg(self):
        basket_info_alert_text = self.get_attribute_of_elem(*ProductPageLocators.ALERT_ABOUT_BASKET_SUM,
                                                                    "innerText")
        item_price = self.get_attribute_of_elem(*ProductPageLocators.ITEM_PRICE, "textContent")
        assert f'Your basket total is now {item_price}' in basket_info_alert_text, "Wrong price in alert"