from domainer.www.google import Googlecheck
from domainer.www.bing import Bingcheck
from domainer.dictionary.dict_attack import DictionaryAttack

class Runsearches:
    def __init__(self, www, dns, dic, all):
        self.do_www = www
        self.do_dns = dns
        self.do_dic = dic
        self.do_all = all
        
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
            
            if google.test_connection():
                for d in google.get_domains(domain):
                    if d not in domains:
                        domains += [d]
                            
            if bing.test_connection():
                for d in bing.get_domains(domain):
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