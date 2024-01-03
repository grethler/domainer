import os
import subprocess

class DictionaryAttack:
    def __init__(self, strength):
        self.strength = strength

    def get_domains(self, domain):
        """
        This function uses a dictionary to test different domains.
        """

        domain = f".{domain}"
        domains = []
        strength = ""
        available_Domains = []
        print("[i] Starting dictionary attack...")

        if self.strength == "1":
            strength = "1000"
        elif self.strength == "2":
            strength = "10000"
        elif self.strength == "3":
            strength = "100000"
        elif self.strength == "4":
            strength = "1000000"

        with open(f"{os.getcwd()}/wordlists/bitquark_20160227_subdomains" +
            f"_popular_{strength}.txt", "r", encoding="utf-8") as f:
            for line in f.readlines():
                domains += [line.strip() + domain]
        for dom in domains:
            try:
                available = True
                try:
                    subprocess.check_output(["ping", f"{dom}", "-n", "1"]) \
                    .decode("utf-8", errors="ignore")
                except subprocess.CalledProcessError:
                    available = False
                if available: 
                    print(f"[+] Domain found: {dom}")
                    available_Domains += [dom]        
            except KeyboardInterrupt:
                break  
        print("[i] Finished.")    
        return(available_Domains)        