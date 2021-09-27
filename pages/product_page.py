from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):

    def promo_product_page(self):
        product_page = self.browser.find_element(By.XPATH,"//button[@class = 'btn btn-lg btn-primary btn-add-to-basket']")
        product_page.click()
        # return BasePage(browser=self.browser, url=self.browser.current_url


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_additional_massage(self):
        main_book_name = self.browser.find_element(By.XPATH,"//div[contains(@class,'product_main')]/h1").text
        print(main_book_name)
        added_book_name = self.browser.find_element(By.XPATH,"//div[@id = 'messages'] /div/div/strong").text
        assert main_book_name == added_book_name ,"Its not the same book"


    def correct_price(self):
        cart_price = self.browser.find_element(By.XPATH,'//div[contains(@class, "alert-info")]/div/p/strong').text
        print(cart_price)
        main_price = self.browser.find_element(By.XPATH,'//div[@class = "col-sm-6 product_main"]/p').text

        assert cart_price == main_price , "not the same price"







