#!/usr/bin/env python3
#
# Florian Grethler 2023
# info@florian-grethler.de
# www.florian-grethler.de

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager

class Greq:
    def __init__(self):
        opts = Options()
        opts.add_argument("--headless")
        opts.add_argument("--disable-gpu")
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=opts)
        
    def test_connection(self):
        stat = True
        try:
            requests.get("https://www.google.com/")
        except:
            sat = False
        return stat
    
    def check_element(self, element):
        available = True
        try:
            self.browser.find_element(element[0], element[1])
        except NoSuchElementException:
            try:
                self.browser.execute_script("""const elements = document.getElementsByClassName("yS1nld");
                                            while (elements.length > 0) elements[0].remove();""")
                self.browser.execute_script("""const element = document.getElementById("RP3V5c");
                                            if (element !== null) element.remove();""")
                self.browser.find_element(element[0], element[1])
            except NoSuchElementException:
                available = False
        return(available)
        
    def get_urls(self, domain):  
        self.browser.get("https://www.google.com/search?q=site%3A" + domain)
        urls = []
            
        while(True):
            captcha_present = self.check_element([By.ID, "recaptcha-checkbox-border"])
            if captcha_present:
                self.browser.find_element(By.ID, "recaptcha-checkbox-border").click()
            cookies_present = self.check_element([By.ID, "W0wltc"])
            if cookies_present:
                cookiebtn = self.browser.find_element(By.ID, "W0wltc").click()
                    
            next_page_available = self.check_element([By.ID, "pnnext"])
            if next_page_available:
                for url in self.browser.find_elements(By.CLASS_NAME, "qLRx3b"):
                    if url.text != "":
                        cleaned_url = url.text.replace("...", "").replace(" ", "")
                        try:
                            idx = cleaned_url.index("\u203a")
                        except ValueError:
                            pass
                        cleaned_url = cleaned_url[:idx].split("://")[-1]
                        if cleaned_url not in urls:
                            urls += [cleaned_url]
                self.browser.find_element(By.ID, "pnnext").click()
            else:
                break
            
        self.browser.quit()
        return(urls)