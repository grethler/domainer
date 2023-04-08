#!/usr/bin/env python3
#
# Florian Grethler 2023
# Github: @delsyst0m
# info@florian-grethler.de
# www.florian-grethler.de

import time
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager

class Googlecheck:
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
        """This funtion test if one can connect to the site.
        """
        stat = True
        try:
            response = requests.get("https://www.google.com/")
            if not response.ok:
               raise Exception 
        except Exception:
            stat = False
        return stat
    
    def check_element(self, element):
        """This function checks if an element is available.
        """
        available = True
        try:
            self.browser.find_element(element[0], element[1])
        except NoSuchElementException:
            try:
                self.browser.execute_script(
                    """const elements = document.getElementsByClassName("yS1nld");
                        while (elements.length > 0) elements[0].remove();""")
                self.browser.execute_script(
                    """const element = document.getElementById("RP3V5c");
                        if (element !== null) element.remove();""")
                self.browser.find_element(element[0], element[1])
            except NoSuchElementException:
                available = False
        return(available)
        
    def get_urls(self, domain):
        """This function gets the domains from each site of the search.
        """  
        urls = []
        num = 0   
        entries = ""
        
        while(True):
            progress = ""
            #if not cookie:
            #    cookie = self.browser.get_cookie("GOOGLE_ABUSE_EXEMPTION")      
            #self.browser.add_cookie(cookie)
            
            self.browser.get("https://www.google.com/search?q=site%3A" 
                             + domain + "&start=" + str(num))
            if self.check_element([By.ID, "recaptcha-checkbox-border"]):
                self.browser.find_element(By.ID, 
                                          "recaptcha-checkbox-border").click()
                
            if self.check_element([By.ID, "W0wltc"]):
                self.browser.find_element(By.ID, "W0wltc").click()
            
            if num == 0:
                entries = int((self.browser.find_element(By.ID,
                                                         "result-stats").text)
                              .split(" ")[1].replace(".", ""))
                    
            for url in self.browser.find_elements(By.TAG_NAME, "cite"):
                if url.text and domain in url.text:
                    # removes protocol
                    cleaned_url = url.text.split("//")[-1]
                    try:
                        idx = cleaned_url.index("\u203a")
                        cleaned_url = cleaned_url[:idx]  
                    except ValueError:
                        pass   
                    if cleaned_url not in urls:
                        urls += [cleaned_url]
                  
            time.sleep(2)
            num += 10
            progress += "Progress: ["
            perc = int(50*(num/entries))
            for i in range(perc):
                progress += "X"
            for i in range(50-perc):
                progress += "-"
            progress += "]"
            print(progress, end="\r")
            
            if not self.check_element([By.ID, "pnnext"]):
                print("\n")
                break
            
        self.browser.quit()
        return(urls)