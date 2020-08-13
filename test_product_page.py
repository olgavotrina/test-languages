import time

import pytest

from pages.locators import ProductPageLocators
from pages.main_page import MainPage
from pages.product_page import ProductPage


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com"
                                               "/catalogue/coders-at-work_207/?promo=offer7",
                                               marks=pytest.mark.xfail(reason="bug in promo")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_basket()
    product_page.solve_quiz_and_get_code()
    success_alert_text = product_page.get_attribute_of_elem(*ProductPageLocators.ALERT_ITEM_ADDED, "innerText")
    basket_info_alert_text = product_page.get_attribute_of_elem(*ProductPageLocators.ALERT_ABOUT_BASKET_SUM,
                                                                "innerText")
    item_name = product_page.get_attribute_of_elem(*ProductPageLocators.ITEM_NAME, "textContent")
    item_price = product_page.get_attribute_of_elem(*ProductPageLocators.ITEM_PRICE, "textContent")
    assert f'{item_name} has been added to your basket' in success_alert_text, "Wrong book name in alert"
    assert f'Your basket total is now {item_price}' in basket_info_alert_text, "Wrong price in alert"
