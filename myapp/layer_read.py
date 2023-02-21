import argparse
from bs4 import BeautifulSoup
from .event_src import Event1,Event3,Event5,Event7,Event8,Event10,Event11,Event12,Event15,Event17,Event22
from .get_tecs import Get_Techniques

class layer_reader:
    def __init__(self,layer,excludes,ips):
        self.layer = layer
        self.excludes = excludes
        self.ips = ips
        self.gen()

    def gen(self):
        with open('myapp/Config.xml', 'r') as f:
            config = f.read()
        Bs_config = BeautifulSoup(config, 'xml')

        tecs_obj = Get_Techniques(self.layer)
        tecs = tecs_obj.tecs

        excludes = [0] * 28

        if self.excludes:
            for e in self.excludes:
                excludes[int(e)-1] = 1

         #eventos que quiere tener excludes
        ##Función que extraiga a partir de las técnicas los eventos que hay que recorrer
        ev1 = Event1.event_1(Bs_config,tecs,excludes[0])
        ev3 = Event3.event_3(Bs_config,tecs,excludes[2])
        ev5 = Event5.event_5(Bs_config,tecs,excludes[4])
        ev7 = Event7.event_7(Bs_config,tecs,excludes[6])
        ev8 = Event8.event_8(Bs_config,tecs,excludes[7])
        ev10 = Event10.event_10(Bs_config,tecs,excludes[9])
        ev11 = Event11.event_11(Bs_config,tecs,excludes[10])
        ev12 = Event12.event_12(Bs_config,tecs,excludes[11])
        ev15 = Event15.event_15(Bs_config,tecs,excludes[14])
        ev17 = Event17.event_17(Bs_config,tecs,excludes[16])
        ev22 = Event22.event_22(Bs_config,tecs,excludes[21])


        savechanges = Bs_config.renderContents()
        with open("myapp/Config_final.xml", "wb") as file:
            file.write(savechanges)

