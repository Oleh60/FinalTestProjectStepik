from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import AddingMessageLocator


class NegativeProduct(BasePage):


    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        adding_product = self.browser.find_element(*AddingMessageLocator.ADD_BUTTON_LOCATOR)
        adding_product.click()
        assert self.is_not_element_present(*AddingMessageLocator.ADD_MASSAGE_LOCATOR), "Message is " \
                                                                                                        "present "

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*AddingMessageLocator.ADD_MASSAGE_LOCATOR), "Message is present"


    def message_disappeared_after_adding_product_to_basket(self):
        adding_product = self.browser.find_element(*AddingMessageLocator.ADD_BUTTON_LOCATOR)
        adding_product.click()
        assert self.is_disappeared(*AddingMessageLocator.ADD_MASSAGE_LOCATOR), "Message Still on the " \
                                                                                                "place "
