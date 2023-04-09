#!/usr/bin/env python3
#
# Florian Grethler 2023
# Github: @delsyst0m
# info@florian-grethler.de
# www.florian-grethler.de

import os
import subprocess

class DictionaryAttack:
    def __init__(self, strength):
        self.strength = strength
        
    def get_domains(self, domain):
        """This function uses a dictionary to
        test different domains.
        """
        
        domain = f".{domain}"
        domains = []
        strength = ""
        available_Domains = []
        progress = ""
        
        if self.strength == "1":
            strength = "1000"
        elif self.strength == "2":
            strength = "10000"
        elif self.strength == "3":
            strength = "100000"
        elif self.strength == "4":
            strength = "1000000"
            
        with open(f"{os.getcwd()}bitquark_20160227_subdomains \
            _popular_{strength}.txt", "r", encoding="utf-8") as f:
            for line in f.readlines():
                domains += [line.strip() + domain]
                
        entries = len(domains)
        idx = 1
        
        for dom in domains:
            available = True
            
            progress += "\rDictionary progress: ["
            perc = int(50*(idx/entries))
            for i in range(perc):
                progress += "X"
            for i in range(50-perc):
                progress += "-"
            progress += "]"
            print(progress, end="")
            idx += 1
            
            try:
                subprocess.check_output(["ping", f"{dom}", "-n", "1"]) \
                .decode("utf-8", errors="ignore")
            except subprocess.CalledProcessError:
                available = False
            if available: 
                available_Domains += [dom]
        
        return(available_Domains)        