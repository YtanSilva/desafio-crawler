from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.settings import Settings


class DriverManager:
    @staticmethod
    def get_driver():
        # Instanciando o navegador
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(
            service=service,
            options=Settings.get_chrome_options()
        )
        driver.set_page_load_timeout(Settings.PAGE_LOAD_TIMEOUT)
        driver.implicitly_wait(Settings.IMPLICIT_WAIT)
        return driver