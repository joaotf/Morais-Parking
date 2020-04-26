import pprint;
from os import system;

def Show(estacionamento):
    system('clear');
    pp = pprint.PrettyPrinter(indent=0);
    pp.pprint(estacionamento);