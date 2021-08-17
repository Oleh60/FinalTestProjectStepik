from .base_page import BasePage
class MainBase(base_page.BasePage):

    def __init__(self,browser,link):
        self.browser = browser
        self.link = link
        self.base_page =

    def test_guest_can_go_to_login_page(self,browser,link):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(self.link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()


    # def go_to_login_page(browser):
    # login_link = browser.find_element_by_css_selector("#login_link")
    # login_link.click()

# def test_guest_can_go_to_login_page(browser):
#    browser.get(link)
#    go_to_login_page(browser)