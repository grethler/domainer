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
from selenium.common.exceptions import ElementNotInteractableException
from webdriver_manager.firefox import GeckoDriverManager

class Bingcheck:
    def __init__(self):
        opts = Options()
        opts.add_argument("--headless")
        opts.add_argument("--disable-gpu")
        firefox_profile = FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=opts,
                                         firefox_profile=firefox_profile)
        
    def test_connection(self):
        stat = True
        try:
            response = requests.get("https://www.bing.com/")
            if not response.ok:
               raise Exception 
        except:
            stat = False
        return stat
    
    def check_element(self, element):
        available = True
        try:
            self.browser.find_element(element[0], element[1])
        except NoSuchElementException:
            available = False
        return(available)
    
    def get_urls(self, domain):  
        number = 1
        urls = []
        pagelements=""
          
        while(True):
            self.browser.get("https://www.bing.com/search?q=site%3A" + domain + "&first=" + str(number))
                
            if self.check_element([By.ID, "bnp_cookie_banner"]):
                self.browser.execute_script("""const element = document.getElementById("bnp_cookie_banner");
                                            if (element !== null) element.remove();""")
            print   
            """if self.check_element([By.ID, "bnp_btn_reject"]):
                #self.browser.add_cookie({"name":"BCP","value":"AD=0&AL=0&SM=0","secure":True, "domain":".bing.com"})
                for i in range(4): self.browser.refresh()
                try:
                    self.browser.find_element(By.ID, "bnp_btn_reject").click()
                except ElementNotInteractableException:
                    self.browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/button[2]").click()"""
            
            for url in self.browser.find_elements(By.TAG_NAME, "cite"):
                if url.text and domain in url.text:
                    cleaned_url = (url.text).split("://")[-1].split(domain)[0] + domain
                    if cleaned_url not in urls:
                        urls += [cleaned_url]
            time.sleep(1)        
            if self.browser.find_element(By.CLASS_NAME, "sb_count").text == pagelements:
                break
            else:
                pagelements = self.browser.find_element(By.CLASS_NAME, "sb_count").text
                
            number += 30
        self.browser.quit()
        return(urls)