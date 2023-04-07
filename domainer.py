#!/usr/bin/env python3
#
# Florian Grethler 2023
# Github: @delsyst0m
# info@florian-grethler.de
# www.florian-grethler.de

import sys

from domainer.runsearches import Runsearches

class Domainer:
    
    def logo(self):
        print("      _                       _\n" +                 
            "     | |                     (_)\n"+                
            "   __| | ___  _ __ ___   __ _ _ _ __   ___ _ __\n"+ 
            "  / _` |/ _ \| '_ ` _ \ / _` | | '_ \ / _ \ '__|\n"+
            " | (_| | (_) | | | | | | (_| | | | | |  __/ |\n"+   
            "  \__,_|\___/|_| |_| |_|\__,_|_|_| |_|\___|_|\n\n"+
            "Made by Florian Grethler @delsyst0m\n"+
            "info@florian-grethler.de\n"+
            "www.florian-grethler.de\n\n"                                                 
            )
    
    def askexport(self, domains):
        export  = input("\nDo you want to export them? (Y/N)\n")
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
        
        domainname = input("Please enter a domain (e.g. abcdef.xyz):\n")

        print("\nSearching for subdomains of: " + domainname)
        
        start = Runsearches()
        domains = start.searches(domainname)
        
        print("\nA total of " + str(len(domains)) +  " domains have been found!")
        self.askexport(domains)   
        
if __name__ == "__main__":
    d = Domainer()
    d.main()