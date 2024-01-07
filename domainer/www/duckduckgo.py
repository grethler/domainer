import warnings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager

warnings.filterwarnings("ignore", category=DeprecationWarning) 

class Duckduckgocheck:
    def __init__(self, logger):
        opts = Options()
        opts.add_argument("--headless")
        opts.add_argument("--disable-gpu")
        opts.set_preference('intl.accept_languages', 'en-GB')
        firefox_profile = FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart",
                                        True)
        self.browser = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()), 
            options=opts,
            firefox_profile=firefox_profile)
        self.logger = logger

    def check_element(self, element):
        available = True
        try:
            self.browser.find_element(element[0], element[1])
        except NoSuchElementException:
            available = False
        return(available)

    def get_domains(self, domain):  
        urls = []
        print("[i] Starting DuckDuckGo search...")
        self.browser.get("https://duckduckgo.com/?q=site%3A" + 
                                domain)
        while(True):
            try:
                self.browser.execute_script("window.scrollTo \
                    (0, document.body.scrollHeight);")

                for url in self.browser.find_elements(By.CLASS_NAME, 
                                                        "Rn_JXVtoPVAFyGkcaXyK"):
                    if url.text and domain in url.text:
                        cleaned_url = (url.text).split("://")[-1].split(domain)[0] \
                        + domain
                        if cleaned_url not in urls:
                            urls += [cleaned_url]
                try:
                    self.browser.find_element(By.CLASS_NAME, 
                                                "wE5p3MOcL8UVdJhgH3V1").click()         
                except NoSuchElementException:
                    break

            except Exception as e:
                self.logger.error(f"Couldn't read DuckDuckGo: {e}")
                break

        self.browser.quit()
        print("[i] Finished.")   
        return(urls)