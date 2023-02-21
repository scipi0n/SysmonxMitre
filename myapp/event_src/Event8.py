from bs4 import BeautifulSoup, Comment
from functools import reduce
class event_8:
    def __init__(self, config_soup, tecs, excludes):
        self.soup = config_soup
        self.tecs = tecs
        self.excludes = excludes
        self.write_file()

    def write_file(self):
        #EVENTO 8
        with open('myapp/sysmon_events_rules/Event8.xml', 'r') as f:
            event = f.read()
        Bs_event = BeautifulSoup(event, 'xml')
        conjunto = []
        for t in self.tecs:
            b_rl = Bs_event.find_all('Rule', {'name': t})
            if b_rl: conjunto.append(b_rl)
            b_im = Bs_event.find_all('Image', {'name': t})
            if b_im: conjunto.append(b_im)
            b_si = Bs_event.find_all('SourceImage', {'name': t})
            if b_si: conjunto.append(b_si)
        if conjunto:
            single_list = reduce(lambda x, y: x + y + ['\n'], conjunto)
            Bs_event.CreateRemoteThread.extend(single_list)
            res = Bs_event.find_all('RuleGroup', {'name': '8_include'})
            #comments = Bs_event.find_all(string=lambda text: isinstance(text, Comment))
            #self.soup.EventFiltering.extend(Bs_event.comment1)
            self.soup.EventFiltering.extend(res)
            #self.soup.EventFiltering.extend(Bs_event.comment2)
        if self.excludes == 1:
            rules_exclude = Bs_event.find_all('RuleGroup',{'name': '8_exclude'})
            self.soup.EventFiltering.extend(rules_exclude)

