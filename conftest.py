import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options






def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en or others")

#
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(8)
    yield browser
    print("\nquit browser..")
    # time.sleep(10)
    browser.quit()