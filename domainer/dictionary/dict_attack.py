import os
import threading
import subprocess

class DictionaryAttack:
    available_Domains: list = []

    def __init__(self, strength: int, threads: int):
        self.strength = strength
        self.threads = threads

    def enumerateList(self, domains: list) -> None:
        """
        Enumerate a list of domains and check if they are available.
        """
        for dom in domains:
            available = True
            try:
                subprocess.check_output(["ping", f"{dom}", "-n", "1"]) \
                .decode("utf-8", errors="ignore")
            except subprocess.CalledProcessError:
                available = False
            if available: 
                print(f"[+] Domain found: {dom}")
                self.available_Domains.append(dom)

    def get_domains(self, domain: str) -> list:
        """
        Does a dictionary attack on the given domain for subdomains.
        """
        domain = f".{domain}"
        domains = []
        strength = ""

        print("[i] Starting dictionary attack...")

        # Set strength based on input
        match self.strength:
            case 1:
                strength = 1000
            case 2:
                strength = 10000
            case 3:
                strength = 100000
            case 4:
                strength = 1000000

        with open(f"{os.getcwd()}/wordlists/bitquark_20160227_subdomains" +
                    f"_popular_{strength}.txt", "r", encoding="utf-8") as f:
            for line in f.readlines():
                domains.append(line.strip() + domain)

        if self.threads > 1:
            # Calculate chunks for threading
            avg = len(domains) // self.threads
            remainder = len(domains) % self.threads
            result = []
            start = 0

            for i in range(self.threads):
                if i < remainder:
                    end = start + avg + 1
                else:
                    end = start + avg

                result.append(domains[start:end])
                start = end

            threads = []
            for part in result:
                thread = threading.Thread(target=self.enumerateList, args=(part,))
                threads.append(thread)
                thread.start() 

            # Wait for all threads to complete
            for thread in threads:
                thread.join()
        else:
            self.enumerateList(domains)

        print("[i] Dictionary attack finished.")    
        return self.available_Domains