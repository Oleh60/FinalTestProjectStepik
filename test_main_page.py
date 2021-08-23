from .pages.main_page import MainPage


<<<<<<< HEAD
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()
=======

    def test_guest_can_go_to_login_page(self,browser,link):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()

>>>>>>> 25a4d433502c1b20e62245d9aa37265866c54d76

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

<<<<<<< HEAD
=======
# def test_guest_can_go_to_login_page(browser):
#    browser.get(link)
#    go_to_login_page(browser)
>>>>>>> 25a4d433502c1b20e62245d9aa37265866c54d76
