from pages.locators import BasketPageLocators
from pages.product_page import ProductPage


class BasketPage(ProductPage):

    def should_not_be_items_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_AREA), \
            "Items in cart are presented, but should not be"

    def should_be_message_about_empty_cart(self):
        message_text = self.get_attribute_of_elem(*BasketPageLocators.EMPTY_BASKET_MSG, "innerText")
        assert "Your basket is empty" in message_text, "There is no message about empty cart, but should be"

