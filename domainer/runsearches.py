#!/usr/bin/env python3

import urllib.request
from domainer.www.google import Googlecheck
from domainer.www.bing import Bingcheck
from domainer.www.duckduckgo import Duckduckgocheck
from domainer.dictionary.dict_attack import DictionaryAttack

class Runsearches:
    def __init__(self, www, dns, dic, all):
        self.do_www = www
        self.do_dns = dns
        self.do_dic = dic
        self.do_all = all
    
    def check_connection(self, host):
        """This function checks if the host is reachable.
        """
        try:
            urllib.request.urlopen(host)
            return True
        except urllib.error.URLError:
            return False

    def searches(self, domain): 
        """This function takes the arguments and runs the requested searches.
        """
        domains = []
        
        if self.do_all:
            self.do_www = True
            self.do_dns = True
            self.do_dic = "4"
        
        if self.do_www:
            google = Googlecheck()
            bing = Bingcheck()
            ddg = Duckduckgocheck()
            
            if self.check_connection("https://www.google.com/"):
                for d in google.get_domains(domain):
                    if d not in domains:
                        domains += [d]
                            
            if self.check_connection("https://www.bing.com/"):
                for d in bing.get_domains(domain):
                    if d not in domains:
                        domains += [d]
                        
            if self.check_connection("https://www.duckduckgo.com/"):
                for d in ddg.get_domains(domain):
                    if d not in domains:
                        domains += [d]
        
        
        if self.do_dns:
            # Work in progress
            pass
        
        if self.do_dic:
            da = DictionaryAttack(self.do_dic)
            for d in da.get_domains(domain):
                if d not in domains:
                    domains += [d]
        
        return(domains)