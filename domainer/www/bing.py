#!/usr/bin/env python3
#
# Florian Grethler 2023
# Github: @delsyst0m
# info@grethler.ch
# www.grethler.ch

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
        progress = ""
        print("\nStarting Bing search...")
        firstsite = True
        while(True):
            try:
                self.browser.get("https://www.bing.com/search?q=site%3A" + 
                                domain + "&first=" + str(number))
                
                if "There are no results for" in self.browser.page_source:
                    break
                
                if self.check_element([By.CLASS_NAME, "sb_count"]) and not firstsite:
                    nums = self.browser.find_element(By.CLASS_NAME, "sb_count").text.split(" ")
                    entries = int(nums[-2].replace(".",""))
                    num = int(nums[0].split("-")[-1].replace(".",""))
                    perc = int(50*(num/entries))
                    progress += "\r["
                    for i in range(perc):
                        progress += "#"
                    for i in range(50-perc):
                        progress += "."
                    progress += "]"
                    print(progress, end="")
                
                if self.check_element([By.ID, "bnp_cookie_banner"]):
                    self.browser.execute_script(
                    """const element = document.getElementById("bnp_cookie_banner");
                        if (element !== null) element.remove();""")
                
                for url in self.browser.find_elements(By.TAG_NAME, "cite"):
                    if url.text and domain in url.text:
                        cleaned_url = (url.text).split("://")[-1].split(domain)[0] \
                        + domain
                        if cleaned_url not in urls:
                            urls += [cleaned_url]
                time.sleep(1)           
                number += 30
                firstsite = False
            except KeyboardInterrupt:
                break
                        
        self.browser.quit()
        print("Finished.")   
        return(urls)