import time

import pytest

from pages.locators import ProductPageLocators
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_basket()
    product_page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_basket()
    product_page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_cart()
    basket_page.should_be_message_about_empty_cart()


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "12345678QWw!"
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = MainPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
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
