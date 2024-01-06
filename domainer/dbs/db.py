import time
import json
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

class CheckDBs:
    def __init__(self, domain: str):
        self.domain = domain
        self.available_Domains: list[str] = []
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

    def checkWhoisXML(self) -> None:
        try:
            print("[i] Checking WhoisXML db")
            self.browser.get("https://subdomains.whoisxmlapi.com/api")
            div_path = "/html/body/div[3]/section/div/div/div[2]/div/form/div[2]/div/input"
            input_field = self.browser.find_element(By.XPATH, div_path)
            input_field.send_keys(Keys.CONTROL + "a")
            input_field.send_keys(Keys.DELETE)
            input_field.send_keys(self.domain)
            input_field.submit()
            time.sleep(10)
            response = self.browser.find_element(By.CLASS_NAME, "json")
            response = json.loads(response.text)
            for domain in response["result"]["records"]:
                self.available_Domains.append(domain["domain"])
                print("[i] Finished checking WhoisXML db.")
        except Exception as e:
            print("[!] Couldn't read WhoisXML db")

    def get_domains(self) -> list[str]:
        """
        Uses different dbs and returns a list of found domains.
        """
        self.checkWhoisXML()
        return self.available_Domains