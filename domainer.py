import sys
import argparse
import logging
import urllib.request
from domainer.runsearches import Runsearches

class Domainer:

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.ERROR)
        logging.basicConfig(filename="./domainer/logs/domainer.log")
        self.formatter = logging.Formatter("[%(asctime)s] %(message)s")
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.stream_handler)

    def logo(self) -> None:
        """
        This function prints the logo of the script.
        """
        print("\n __/ _  ____ __   o __ _  __ \n"
            "(_/_(_)/ / /(_/|_/_/ /(<_/ (_\n"+
            "Made by Florian Grethler\n")

    def askexport(self, domains: list) -> None:
        """
        This function asks if the user wants to export the domains as a csv file.
        """
        export  = input("[i] Do you want to export them? (Y/N)\n")
        if export == "Y" or export == "y":
            f = open("domains.csv")
            for i in domains:
                f.write(i + "\n")
        elif export == "N" or export == "n":
            sys.exit(0)
        else:
            self.askexport(domains)

    def main(self, target: str, www: bool, db: bool, dict: int, threads: int) -> None:  
        """
        This is the start function of domainer.
        """      
        self.logo()

        print(f"[i] Searching for subdomains of: {target}")
        #print("[i] Step may be stopped with CTRL+C")
        start = Runsearches(www=www, db=db, dic=dict, 
                            threads=threads, logger=self.logger)
        domains = start.searches(target)
        if len(domains) > 0: 
            print("[i] A total of " + str(len(domains)) +  " domains have been found!")
            self.askexport(domains)   
        else:
            sys.exit("[!] No domains found!")
        # add checking here

if __name__ == "__main__":
    argp = argparse.ArgumentParser()
    argp.add_argument("-w", "--www", default=False, action="store_true", 
                    help="use web search")
    argp.add_argument("-d", "--dict", default="0", type=str,
                    help="use dictionary attack; difficulty '1'-'4'")
    argp.add_argument("-t", "--threads", default="0", type=str, 
                    help="Number of threads used for dictionary attack")
    argp.add_argument("-b", "--db", default=False, action="store_true", 
                    help="use db search")
    argp.add_argument("target", type=str,
                    help="Target for example: abcdefg.xyz")
    args = argp.parse_args()

    args.threads = int(args.threads)
    args.dict = int(args.dict)
    
    if not args.www and not args.dict and not args.db:
        sys.exit("[!] Script needs at least one argument besides the target!")

    if args.dict and (int(args.dict) < 1 or int(args.dict) > 4):
        sys.exit("[!] Dictionary attack difficulty must be between 1 and 4!") 

    if args.threads and args.threads < 1:
        sys.exit("[!] Number of threads must be at least 1!")

    if args.threads and not args.dict:
        sys.exit("[!] Number of threads can only be used with dictionary attack!")

    try:
        urllib.request.urlopen("https://www.google.com/")
    except urllib.error.URLError:
        sys.exit("[!] Couldn't connect to internet." +
                    " Please try again later or check your network settings.")

    d = Domainer()
    d.main(target=args.target, www=args.www, db=args.db, 
           dict=args.dict, threads=args.threads)