from domainer.www.google import Googlecheck
from domainer.www.bing import Bingcheck

class Runsearches:
    def searches(self, domain): 
        google = Googlecheck()
        bing = Bingcheck()
        
        domains = []
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
                    
        return(domains)