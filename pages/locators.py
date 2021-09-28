from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_PAGE_LOCATOR = (By.XPATH, '//form[@id = "login_form"]')

    registr_locator = (By.XPATH, '//form[@id = "register_form"]')

    EMAIL_LOCATOR = (By.XPATH,"//input[@id = 'id_registration-email']")

    PASSWORD_LOCATOR = (By.XPATH,"//input[@id = 'id_registration-password1']")

    #another password form to make registration
    PASSWORD_LOCATOR1 = (By.XPATH,"//input[@id = 'id_registration-password2']")

    CONFIRM_BUTTON_LOCATOR = (By.XPATH,"//button[@name = 'registration_submit']")

class StafLocators():
    STAF_Link = (By.XPATH, '//a[@class = "dropdown-toggle"]')


class StafAddLocators():


    book1_add_locator = (By.XPATH, "//button[@class = 'btn btn-lg btn-primary btn-add-to-basket']")


class AddingMessageLocator():
    ADD_MASSAGE_LOCATOR = (By.XPATH, "//div[@id = 'messages'] /div/div/strong")

    ADD_BUTTON_LOCATOR = (By.XPATH, '//form[@id = "add_to_basket_form"]/button')

    ADD_HEADER_MESSAGE_LOCATOR = (By.XPATH, "//div[contains(@class,'product_main')]/h1")


class BasePageLocators():
    LOGIN_LINK = (By.XPATH, '//a[@id = "login_link"]')
    USER_ICON = (By.XPATH, "//i[@class ='icon-user']")
    # LOGIN_LINK_INVALID = (By.XPATH, '//*[@id ="login_link_inc"]')


class BasketLocator():
    BASKET_LINK = (By.XPATH, '//a[@class ="btn btn-default"]')

    PRODUCT_CONFIRM_LOCATOR = (By.XPATH,'//div[@class = "basket-title hidden-xs"]')
