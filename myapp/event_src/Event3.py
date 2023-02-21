from bs4 import BeautifulSoup
from functools import reduce
class event_3:
    def __init__(self, config_soup, tecs, excludes):
        self.soup = config_soup
        self.tecs = tecs
        self.excludes = excludes
        self.write_file()

    def write_file(self):
        #EVENTO 3
        with open('myapp/sysmon_events_rules/Event3.xml', 'r') as f:
            event = f.read()
        Bs_event = BeautifulSoup(event, 'xml')
        conjunto = []
        for t in self.tecs:
            b_dp = Bs_event.find_all('DestinationPort',{'name' : t})
            if b_dp: conjunto.append(b_dp)
            b_sp = Bs_event.find_all('SourcePort', {'name': t})
            if b_sp: conjunto.append(b_sp)
            b_rl = Bs_event.find_all('Rule', {'name': t})
            if b_rl: conjunto.append(b_rl)
            b_im = Bs_event.find_all('Image', {'name': t})
            if b_im: conjunto.append(b_im)
        if conjunto:
            single_list = reduce(lambda x, y: x + y + ['\n'], conjunto)
            Bs_event.NetworkConnect.extend(single_list)
            res = Bs_event.find_all('RuleGroup', {'name': '3_include'})
            self.soup.EventFiltering.extend(res)
        if self.excludes == 1:
            rules_exclude = Bs_event.find_all('RuleGroup',{'name': '3_exclude'})
            self.soup.EventFiltering.extend(rules_exclude)

