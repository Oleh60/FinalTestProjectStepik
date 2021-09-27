from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_locator = (By.XPATH,'//form[@id = "login_form"]')

    registr_locator = (By.XPATH,'//form[@id = "register_form"]')

class StafLocators():
    STAF_Link = (By.XPATH,'//a[@class = "dropdown-toggle"]')

class StafAddLocators():

    # allbooks_locator = (By.XPATH,'//a[@href= "/uk/catalogue/"]')

    book1_add_locator = (By.XPATH,"//button[@class = 'btn btn-lg btn-primary btn-add-to-basket']")

