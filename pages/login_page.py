from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
from selenium.webdriver.common.by import By




class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):

        assert "login" in self.browser.current_url, "not correct url, try to choose login page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_PAGE_LOCATOR), "there is no login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.registr_locator), "there is no registration form"

    def register_new_user(self, email, password):
        user_login_step1 = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        user_login_step1.click()
        user_email = self.browser.find_element(*LoginPageLocators.EMAIL_LOCATOR)
        user_email.send_keys(email)
        user_password = self.browser.find_element(*LoginPageLocators.PASSWORD_LOCATOR)
        user_password.send_keys(password)
        user_password1 = self.browser.find_element(*LoginPageLocators.PASSWORD_LOCATOR1)
        user_password1.send_keys(password)
        user_registration = self.browser.find_element(*LoginPageLocators.CONFIRM_BUTTON_LOCATOR)
        user_registration.click()








