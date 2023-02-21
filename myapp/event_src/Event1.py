from bs4 import BeautifulSoup
from functools import reduce
class event_1:
    def __init__(self, config_soup, tecs, excludes):
        self.soup = config_soup
        self.tecs = tecs
        self.excludes = excludes
        self.write_file()


    def write_file(self):
        #EVENTO 1
        with open('myapp/sysmon_events_rules/Event1.xml', 'r') as f:
            event = f.read()
        Bs_event = BeautifulSoup(event, 'xml')
        conjunto = []
        for t in self.tecs:
            b_pi = Bs_event.find_all('ParentImage',{'name' : t})
            if b_pi: conjunto.append(b_pi)
            b_cl = Bs_event.find_all('CommandLine', {'name': t})
            if b_cl: conjunto.append(b_cl)
            b_rl = Bs_event.find_all('Rule', {'name': t})
            if b_rl: conjunto.append(b_rl)
            b_of = Bs_event.find_all('OriginalFileName', {'name': t})
            if b_of: conjunto.append(b_of)
            b_im = Bs_event.find_all('Image', {'name': t})
            if b_im: conjunto.append(b_im)
        if conjunto:
            single_list = reduce(lambda x, y: x + y + ['\n'], conjunto)
            Bs_event.ProcessCreate.extend(single_list)
            res = Bs_event.find_all('RuleGroup', {'name': '1_include'})
            self.soup.EventFiltering.extend(res)

        if self.excludes == 1:
            rules_exclude = Bs_event.find_all('RuleGroup',{'name': '1_exclude'})
            self.soup.EventFiltering.extend(rules_exclude)

