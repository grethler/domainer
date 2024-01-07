import time
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager

warnings.filterwarnings("ignore", category=DeprecationWarning) 

class Yahoocheck:
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
        number = 1
        urls = []
        print("[i] Starting Yahoo search...")
        self.browser.get("https://search.yahoo.com/search?p=site%3A"+
                                 domain + "&b=" + str(number))
        # Remove cookie window
        path= "/html/body/div/div/div/div/div/button"
        self.browser.find_element(By.XPATH, path).click()
        path = "/html/body/div/div/div/div/form/div[2]/div[2]/button[2]"
        self.browser.find_element(By.XPATH, path).click()
        while(True):
            try:
                self.browser.get("https://search.yahoo.com/search?p=site%3A"+
                                 domain + "&b=" + str(number))

                if "Check spelling or type a new query." in self.browser.page_source:
                    break

                class_name = "d-ib.p-abs.t-0.l-0"
                for url in self.browser.find_elements(By.CLASS_NAME, class_name):
                    if url.text and domain in url.text:
                        cleaned_url = url.text
                        try:
                            idx = cleaned_url.index("\u203a")   
                            cleaned_url = cleaned_url[:idx]
                            print(cleaned_url)
                        except ValueError:
                            pass   
                        if cleaned_url not in urls:
                            urls += [cleaned_url]
                number += 7
            except Exception as e:
                self.logger.error(f"Couldn't read Yahoo: {e}")
                break

        self.browser.quit()
        print("[i] Finished.")   
        return(urls)