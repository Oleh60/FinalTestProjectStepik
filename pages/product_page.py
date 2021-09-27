from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import AddingMessageLocator, BasePageLocators
from selenium.common.exceptions import NoAlertPresentException

import math


class ProductPage(BasePage):

    def promo_product_page(self):
        product_page = self.browser.find_element(By.XPATH,
                                                 "//button[@class = 'btn btn-lg btn-primary btn-add-to-basket']")
        product_page.click()

        # return BasePage(browser=self.browser, url=self.browser.current_url

    def should_be_additional_massage(self):
        main_book_name = self.browser.find_element(By.XPATH, "//div[contains(@class,'product_main')]/h1").text
        print(main_book_name)
        added_book_name = self.browser.find_element(*AddingMessageLocator.add_massege_locator).text
        assert main_book_name == added_book_name, "Its not the same book"

    def correct_price(self):
        cart_price = self.browser.find_element(By.XPATH, '//div[contains(@class, "alert-info")]/div/p/strong').text
        print(cart_price)
        main_price = self.browser.find_element(By.XPATH, '//div[@class = "col-sm-6 product_main"]/p').text

        assert cart_price == main_price, "not the same price"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "User probably dont see login form"

    def go_to_login_page_from_product_page(self):
        self.go_to_login_page()
        login_form = self.is_element_present(By.XPATH, '//form[@id = "login_form"]')
        assert login_form == True, "There is no login form"
