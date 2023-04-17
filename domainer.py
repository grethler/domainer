#!/usr/bin/env python3
#
# Florian Grethler 2023
# Github: @delsyst0m
# info@florian-grethler.de
# www.florian-grethler.de

import sys
import argparse
from domainer.runsearches import Runsearches

argp = argparse.ArgumentParser()
argp.add_argument("-w", "--www", default=False, action="store_true", 
                  help="use web search")
argp.add_argument("-d", "--dict", default="", type=str,
                  help="use dictionary attack difficulty '1'-'4'")
argp.add_argument("-n", "--dns", default=False, action="store_true", 
                  help="use dns search")
argp.add_argument("-A", default=False, action="store_true", 
                  help="Use all searches and attacks \
                  (Dictionary attack strength: '4')")
argp.add_argument("target", type=str,
                  help="Target for example: abcdefg.xyz")
args = argp.parse_args()
    
class Domainer:
    
    def logo(self):
        """This function prints the logo of the script.
        """
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
        """This function asks if the user wants to export the domains as a csv file.
        """
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
        """This is the start function of domainer.
        """      
        self.logo()
        
        domainname = args.target
        
        print("Searching for subdomains of: " + domainname)
        
        start = Runsearches(www=args.www, dns=args.dns, dic=args.dict, all=args.A)
        domains = start.searches(domainname)
        print("\n")
        for dom in domains:
            print(dom)
        print("\nA total of " + str(len(domains)) +  " domains have been found!")
        if len(domains) != 0:
            self.askexport(domains)   
        
if __name__ == "__main__":
    if not args.www and not args.dict and not args.dns and not args.A:
        sys.exit("Script needs at least one argument besides the target!")
        
    d = Domainer()
    d.main()