#!/usr/bin/env python3
#
# Florian Grethler 2023
# Github: @delsyst0m
# info@florian-grethler.de
# www.florian-grethler.de

import requests
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager

class Bingcheck:
    def __init__(self):
        opts = Options()
        opts.add_argument("--headless")
        opts.add_argument("--disable-gpu")
        opts.set_preference('intl.accept_languages', 'en-GB')
        firefox_profile = FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
        self.browser = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()), 
            options=opts,
            firefox_profile=firefox_profile)
        
    def test_connection(self):
        stat = True
        try:
            response = requests.get("https://www.bing.com/")
            if not response.ok:
               raise Exception 
        except Exception:
            stat = False
        return stat
    
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
        pages = ""
        
        while(True):
            if self.check_element([By.CLASS_NAME, "sb_pagS"]):
                pages = self.browser.find_element(By.CLASS_NAME, 
                                                  "sb_pagS").text 
                
            self.browser.get("https://www.bing.com/search?q=site%3A" + 
                             domain + "&first=" + str(number))
                
            if self.check_element([By.ID, "bnp_cookie_banner"]):
                self.browser.execute_script(
                """const element = document.getElementById("bnp_cookie_banner");
                    if (element !== null) element.remove();""")
            
            for url in self.browser.find_elements(By.TAG_NAME, "cite"):
                if url.text and domain in url.text:
                    cleaned_url = (url.text).split("://")[-1].split(domain)[0] + domain
                    if cleaned_url not in urls:
                        urls += [cleaned_url]
            time.sleep(1)    
            
            number += 30

            #print((self.browser.find_element(By.CLASS_NAME, 
            # "sb_count").text).split(" ")[-2].replace(".",""))
            if pages == self.browser.find_element(By.CLASS_NAME, "sb_pagS").text:
                break            
        self.browser.quit()
        return(urls)