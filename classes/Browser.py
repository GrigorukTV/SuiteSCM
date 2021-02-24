from selenium.webdriver import ChromeOptions, FirefoxOptions
from webdrivermanager import ChromeDriverManager, GeckoDriverManager
from selenium import webdriver



class Browser:
    web_browser = None

    param = {
        'chrome': {
            'driver': ChromeDriverManager,
            'options': ChromeOptions,
            'webdriver': webdriver.Chrome
        },
        'firefox': {
            'driver': GeckoDriverManager,
            'options': FirefoxOptions,
            'webdriver': webdriver.Firefox
        }
    }

    def __init__(self, browser, url):
        self.add_options(browser, url)


    # Окрытие страницы
    def add_options(self, browser, url):
        params = self.param[browser]
        drivers = params['driver']()
        drivers.download_and_install()
        options = params['options']()
        options.headless = True
        self.web_browser = params['webdriver'](options=options)
        self.web_browser.get(url)

    # Получение объекта webdriver
    def get_wd(self):
        return self.web_browser


    # Закрытие браузера
    def closeBrowser(self):
        self.web_browser.quit()
