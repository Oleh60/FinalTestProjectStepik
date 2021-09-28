from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import AddingMessageLocator, BasePageLocators, BasketLocator,LoginPageLocators


import math


class ProductPage(BasePage):

    def promo_product_page(self):
        #promo product locator,dont want to adding in to locator.py
        product_page = self.browser.find_element(By.XPATH,
                                                 "//button[@class = 'btn btn-lg btn-primary btn-add-to-basket']")
        product_page.click()



    def should_be_additional_massage(self):
        main_book_name = self.browser.find_element(*AddingMessageLocator.ADD_HEADER_MESSAGE_LOCATOR).text
        print(main_book_name)
        added_book_name = self.browser.find_element(*AddingMessageLocator.ADD_MASSAGE_LOCATOR).text
        assert main_book_name == added_book_name, "Its not the same book"

    def correct_price(self):
        #promo product locators
        cart_price = self.browser.find_element(By.XPATH, '//div[contains(@class, "alert-info")]/div/p/strong').text
        print(cart_price)
        main_price = self.browser.find_element(By.XPATH, '//div[@class = "col-sm-6 product_main"]/p').text

        assert cart_price == main_price, "not the same price"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "User probably dont see login form"

    def go_to_login_page_from_product_page(self):
        self.go_to_login_page()
        login_form = self.is_element_present(*LoginPageLocators.LOGIN_PAGE_LOCATOR)
        assert login_form == True, "There is no login form"


    def see_product_in_basket_opened_from_main_page(self):
        basket = self.browser.find_element(*BasketLocator.BASKET_LINK)
        basket.click()

        assert self.is_not_element_present(*BasketLocator.PRODUCT_CONFIRM_LOCATOR),"some products present"
        #cant find from where is this locator to add it to locator.py
        assert self.is_element_present(By.XPATH,'//div[@id = "content_inner"]/p'), "The message is not correct"


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


    def can_add_product_to_basket(self):
        adding_product = self.browser.find_element(*AddingMessageLocator.ADD_BUTTON_LOCATOR)
        adding_product.click()
        assert self.is_element_present(*AddingMessageLocator.ADD_MASSAGE_LOCATOR),"Opps,you didnt add the product"

