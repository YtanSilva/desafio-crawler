from selenium.webdriver.chrome.options import Options

class Settings:
    # Configurando WebDriver
    WEBDRIVER_TIMEOUT = 10
    PAGE_LOAD_TIMEOUT = 30
    IMPLICIT_WAIT = 2
    USER_AGENT = 'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    
    # Opcionais do navegador
    @staticmethod
    def get_chrome_options():
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-images')
        options.add_argument('--window-size=1920,1080')
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36')
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        return options
    
    # URLs
    IMDB_TOP_MOVIES_URL = 'https://www.imdb.com/chart/top/'
    IMDB_TOP_DETAIS_URL = 'https://www.imdb.com/'