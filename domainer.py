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
    opt = Options()
    #opt.add_argument()
    #opt.add_argument("--headless")
    opt.add_argument("--disable-gpu")
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=opt)
    
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
            "Released under the Apache v2.0 license\n\n"                                                    
            )
        
    def test_stats(self):
        try:
            requests.get("https://www.google.com/")
        except:
            print("Couldn't connect to server. Make sure to be connected to the internet.")

    def check_element(self, element):
        available = True
        try:
            browser.find_element(element[0], element[1])
        except NoSuchElementException:
            available = False
        return(available)
        
    def get_urls(self, domain):  
        captcha_present = check_element([By.ID, "recaptcha-checkbox-border"])
        if captcha_present:
            captcha.click()

        cookies_present = check_element([By.ID, "W0wltc"])
        if cookies_present:
            button.click()

        urls = []
        next_page_available = check_element([By.ID, "pnnext"])
            
        while(next_page_available):
            captcha_present = check_element([By.ID, "recaptcha-checkbox-border"])
            if captcha_present:
                captcha.click()
            
            for url in browser.find_elements(By.CLASS_NAME, "qLRx3b"):
                if url.text != "":
                    cleaned_url = url.text.replace("...", "").replace(" ", "")
                    idx = cleaned_url.index("\u203a")
                    cleaned_url = cleaned_url[:idx]
                    if cleaned_url not in urls:
                        urls += [cleaned_url]
                
            if next_page_available:
                next_page.click()
            
        print(urls)
        browser.quit()
        
    def main(self, test):
        if test:
            self.test_stats()
        
        self.logo()
        url = input("Please enter a domain without subdomain and protocol:\n")
        
        self.get_urls(url)
        
if __name__ == "__main__":
    d = Domainer()
    d.main(True)