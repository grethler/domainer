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
        firefox_profile = FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=opts,
                                         firefox_profile=firefox_profile)
        
    def test_connection(self):
        stat = True
        try:
            response = requests.get("https://www.google.com/")
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
        urls = []
        num = 0   
        entries = ""
        
        while(True):
            #if not cookie:
            #    cookie = self.browser.get_cookie("GOOGLE_ABUSE_EXEMPTION")      
            #self.browser.add_cookie(cookie)
            
            self.browser.get("https://www.google.com/search?q=site%3A" + domain + "&start=" + str(num))
            if self.check_element([By.ID, "recaptcha-checkbox-border"]):
                self.browser.find_element(By.ID, "recaptcha-checkbox-border").click()
                
            if self.check_element([By.ID, "W0wltc"]):
                self.browser.find_element(By.ID, "W0wltc").click()
            
            if num == 0:
                print(self.browser.find_element(By.ID, "result-stats").text)   
                time.sleep(100000)
                #if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                #print(i)
                # jede seite hat 30 ergebnisse
                # die zahl dann durch 30 = x
                # x <--> 100
                # 1 <--> 100/x
                # num <--> num*(100/x) <--- wie viel bereits durchlaufen
                    
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
            if not self.check_element([By.ID, "pnnext"]):
                break
            
        self.browser.quit()
        return(urls)