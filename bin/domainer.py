#!/usr/bin/env python3
#
# Florian Grethler 2023
# info@florian-grethler.de
# www.florian-grethler.de

import requests
import urllib3
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager

class Domainer:
    def __init__(self):
        opts = Options()
        #opts.add_argument("--headless")
        opts.add_argument("--disable-gpu")
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=opts)
    
    def logo(self):
        print("      _                       _\n" +                 
            "     | |                     (_)\n"+                
            "   __| | ___  _ __ ___   __ _ _ _ __   ___ _ __\n"+ 
            "  / _` |/ _ \| '_ ` _ \ / _` | | '_ \ / _ \ '__|\n"+
            " | (_| | (_) | | | | | | (_| | | | | |  __/ |\n"+   
            "  \__,_|\___/|_| |_| |_|\__,_|_|_| |_|\___|_| v1.0\n\n"+
            "Made by Florian Grethler 2023\n"+
            "info@florian-grethler.de\n"+
            "www.florian-grethler.de\n"+ 
            "Released under the Gnu general public license\n\n"                                                    
            )
        
    def test_stats(self):
        try:
            requests.get("https://www.google.com/")
        except:
            print("Couldn't connect to server. Make sure to be connected to the internet.")

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
        captcha_present = self.check_element([By.ID, "recaptcha-checkbox-border"])
        if captcha_present:
            self.browser.find_element(By.ID, "recaptcha-checkbox-border").click()

        cookies_present = self.check_element([By.ID, "W0wltc"])
        if cookies_present:
            cookiebtn = self.browser.find_element(By.ID, "W0wltc")
            cookiebtn.click()

        self.browser.get("https://www.google.com/search?q=site%3A" + domain)
        urls = []
            
        while(True):
            captcha_present = self.check_element([By.ID, "recaptcha-checkbox-border"])
            if captcha_present:
                self.browser.find_element(By.ID, "recaptcha-checkbox-border").click()
                    
            next_page_available = self.check_element([By.ID, "pnnext"])
            if next_page_available:
                for url in self.browser.find_elements(By.CLASS_NAME, "qLRx3b"):
                    if url.text != "":
                        cleaned_url = url.text.replace("...", "").replace(" ", "")
                        try:
                            idx = cleaned_url.index("\u203a")
                        except ValueError:
                            pass
                        cleaned_url = cleaned_url[:idx]
                        if cleaned_url not in urls:
                            urls += [cleaned_url]
            else:
                break
                
            if next_page_available:
                self.browser.find_element(By.ID, "pnnext").click()
            
        print(urls)
       #self.browser.quit()
        
    def main(self, test):
        if test:
            self.test_stats()
        
        self.logo()
        #url = input("Please enter a domain without subdomain and protocol:\n")
        url = google.com
        print("Searching for subdomains of: " + url)
        self.get_urls(url)
        
if __name__ == "__main__":
    d = Domainer()
    d.main(True)