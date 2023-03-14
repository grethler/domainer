#!/usr/bin/env python3
#
# Florian Grethler 2023
# info@florian-grethler.de
# www.florian-grethler.de

import requests
import urllib3
import sys

from domainer.www.g import Greq

class Domainer:
    
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
    
    def askexport(self, domains):
        export  = input("\nDo you want to export them? (Y/N) ")
        if export == "Y" or export == "y":
            f = open("domains.csv")
            for i in domains:
                f.write(i + "\n")
        elif export == "N" or export == "n":
            sys.exit(0)
        else:
            self.askexport(domains)
            
    def main(self):        
        self.logo()
        g = Greq()
        
        domainname = input("Please enter a domain without subdomain and protocol:\n")
        
        print("\nSearching for subdomains of: " + domainname)
        
        domains = g.get_urls(domainname)
        
        print("\nThe following " + str(len(domains)) +  " domains have been found:")
        
        for domain in domains:
            print(domain)
            
        self.askexport(domains)   
        
if __name__ == "__main__":
    d = Domainer()
    d.main()