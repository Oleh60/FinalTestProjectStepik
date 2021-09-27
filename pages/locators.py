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

class AddingMessageLocator():
    add_massege_locator = (By.XPATH,"//div[@id = 'messages'] /div/div/strong")


class BasePageLocators():
    LOGIN_LINK = (By.XPATH, '//a[@id = "login_link"]')
    # LOGIN_LINK_INVALID = (By.XPATH, '//*[@id ="login_link_inc"]')


