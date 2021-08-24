from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_locator = (By.XPATH,'//form[@id = "login_form"]')

    registr_locator = (By.XPATH,'//form[@id = "register_form"]')
