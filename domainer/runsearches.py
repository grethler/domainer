import urllib.request
from domainer.www.google import Googlecheck
from domainer.www.bing import Bingcheck
from domainer.www.duckduckgo import Duckduckgocheck
from domainer.dictionary.dict_attack import DictionaryAttack

class Runsearches:
    def __init__(self, www: bool, db: bool, dic: int, threads: int):
        self.do_www = www
        self.do_db = db
        self.do_dic = dic
        self.threads = threads

    def check_connection(self, host: str) -> bool:
        """
        This function checks if the host is reachable.
        """
        try:
            urllib.request.urlopen(host)
            return True
        except urllib.error.URLError:
            return False

    def searches(self, domain: str) -> list: 
        """
        This function takes the arguments and runs the requested searches.
        """
        domains = []

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

        if self.do_db:
            # Work in progress
            pass

        if self.do_dic:
            da = DictionaryAttack(self.do_dic, self.threads)
            for d in da.get_domains(domain):
                if d not in domains:
                    domains += [d]

        return(domains)