#!/usr/bin/env python3

import sys
import argparse
from domainer.runsearches import Runsearches
import urllib.request

class Domainer:
    
    def logo(self):
        """This function prints the logo of the script.
        """
        print("\n __/ _  ____ __   o __ _  __ \n"
            "(_/_(_)/ / /(_/|_/_/ /(<_/ (_\n\n"+
            "Made by @grethler)
    
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

    def main(self, target, www, dns, dict, A):  
        """This is the start function of domainer.
        """      
        self.logo()
        
        print(f"Searching for subdomains of: {target}")
        print("(Skip step with CTRL + C)\n")
        start = Runsearches(www, dns, dict, A)
        domains = start.searches(target)
        if len(domains) != 0: 
            print("\n") 
            for dom in domains:
                print(dom)
            print("\nA total of " + str(len(domains)) +  " domains have been found!")
            self.askexport(domains)   
        else:
            sys.exit("No domains found!")
        
if __name__ == "__main__":
    argp = argparse.ArgumentParser()
    argp.add_argument("-w", "--www", default=False, action="store_true", 
                    help="use web search")
    argp.add_argument("-d", "--dict", default="", type=str,
                    help="use dictionary attack; difficulty '1'-'4'")
    argp.add_argument("-n", "--dns", default=False, action="store_true", 
                    help="use dns search")
    argp.add_argument("-A", default=False, action="store_true", 
                    help="Use all searches and attacks \
                    (Dictionary attack strength: '4')")
    argp.add_argument("target", type=str,
                    help="Target for example: abcdefg.xyz")
    args = argp.parse_args()

    if not args.www and not args.dict and not args.dns and not args.A:
        sys.exit("Script needs at least one argument besides the target!")
    
    try:
        urllib.request.urlopen("https://www.google.com/")
    except urllib.error.URLError:
        sys.exit("ERROR: Couldn't connect to internet."+
                 " Please try again later or check your network settings.")
          
    d = Domainer()
    d.main(args.target, args.www, args.dns, args.dict, args.A)
