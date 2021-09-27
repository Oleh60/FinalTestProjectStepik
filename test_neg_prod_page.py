from .pages.negative_test_page import NegativeProduct
import pytest

@pytest.mark.xfail(reason= "not actual")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link1 = "http://selenium1py.pythonanywhere.com/uk/catalogue/hacking-exposed-wireless_208/"
    page = NegativeProduct(browser, link1)
    page.open()
    page.guest_cant_see_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/catalogue/hacking-exposed-wireless_208/"
    page = NegativeProduct(browser, link)
    page.open()
    page.guest_cant_see_success_message()

@pytest.mark.skip(reason= "dont needet")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/catalogue/hacking-exposed-wireless_208/"
    page = NegativeProduct(browser, link)
    page.open()
    page.message_disappeared_after_adding_product_to_basket()
