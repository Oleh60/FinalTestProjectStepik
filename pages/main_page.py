from .base_page import BasePage
from selenium.webdriver.common.by import By
from .login_page import LoginPage
from .locators import BasketLocator



class MainPage(BasePage):
    def see_product_in_basket_opened_from_main_page(self):
        basket = self.browser.find_element(*BasketLocator.BASKET_LINK)
        basket.click()
        basket_empty_message = self.browser.find_element(By.XPATH,'//div[@id = "content_inner"]/p').text

        assert self.is_not_element_present(By.XPATH,'//div[@class = "basket-title hidden-xs"]'),"some products present"
        assert basket_empty_message.find("Ваш кошик пустий.") >= 0, "Your message is no correct"








