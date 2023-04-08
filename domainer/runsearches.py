from domainer.www.google import Googlecheck
from domainer.www.bing import Bingcheck

class Runsearches:
    def __init__(self, www, dns, dic, all):
        self.do_www = www
        self.do_dns = dns
        self.do_dic = dic
        self.do_all = all
        
    def searches(self, domain): 
        domains = []
        
        if self.do_all:
            self.do_www = True
            self.do_dns = True
            self.do_dic = True
        
        if self.do_www:
            google = Googlecheck()
            bing = Bingcheck()
            
            if google.test_connection():
                for d in google.get_urls(domain):
                    if d not in domains:
                        print(d)
                        domains += [d]
                            
            if bing.test_connection():
                for d in bing.get_urls(domain):
                    if d not in domains:
                        print(d)
                        domains += [d]
        
        if self.do_dns:
            # Work in progress
            pass
        
        if self.do_dic:
            # Work in progress
            pass       
        return(domains)