from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import AddingMessageLocator
import pytest

class NegativeProduct(BasePage):


    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        adding_product = self.browser.find_element(By.XPATH, '//form[@id = "add_to_basket_form"]/button')
        adding_product.click()
        assert self.is_not_element_present(By.XPATH, '//div[@id = "messages"]/div/div/strong'), "Message is " \
                                                                                                        "present "

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*AddingMessageLocator.add_massege_locator), "Message is present"
    @pytest.mark.skip(reason= "dont needet")
    def message_disappeared_after_adding_product_to_basket(self):
        adding_product = self.browser.find_element(By.XPATH, '//form[@id = "add_to_basket_form"]/button')
        adding_product.click()
        assert self.is_disappeared(By.XPATH, '//div[@id = "messages"]/div/div/strong'), "Message Still on the " \
                                                                                                "place "
