import re

from common.unit import *
from uncommon.unit import *
from special.unit import *
from rare.unit import *
from legendary.unit import *
from immortal.unit import *
from hidden.unit import *
from alternate.unit import *
from transcended.unit import *

r = luffy_snakeman_transcended
ro = r.__dict__

for key in ro.items():
    if key[0] == "name":
        print("-------------------")
        print(key[0], '=', key[1])
    else:
        x = len(eval(key[1].name).__dict__.items())
        y = eval(key[1].name).__dict__
        if x == 1:
            print('|_' ,'name' + " =", y['name'])
        else:
            n = eval(y['name']).__dict__
            m = len(n)
            for ke in n.items():
                if ke[0] == "name":
                    print('|_' ,ke[0], '=', ke[1])
                else:
                    e = len(eval(ke[1].name).__dict__.items())
                    p = eval(ke[1].name).__dict__
                    if e == 1:
                        print("\t", "|_", 'name' + ":", p['name'])
                    else:
                        j = eval(p['name']).__dict__
                        b = len(j)
                        for k in j.items():
                            if k[0] == "name":
                                print('\t', "|_" ,k[0], '=', k[1])
                            else:
                                ee = len(eval(k[1].name).__dict__.items())
                                pwq = eval(k[1].name).__dict__
                                if ee == 1:
                                    print("\t\t" ,"|_", 'name' + ":", pwq['name'])    
                                else:
                                    ji = eval(pwq['name']).__dict__
                                    ba = len(ji)
                                    for ka in ji.items():
                                        if ka[0] == "name":
                                            print('\t\t','|_' ,ka[0], '=', ka[1])
                                        else:
                                            eevee = len(eval(ka[1].name).__dict__.items())
                                            pwqaa = eval(ka[1].name).__dict__
                                            if eevee == 1:
                                                print("\t\t\t" ,"|_", 'name' + ":", pwqaa['name'])  
                                            else:
                                                jia = eval(pwqaa['name']).__dict__
                                                ban = len(jia)
                                                for kam in jia.items():
                                                    if kam[0] == 'name':
                                                        print('\t\t\t', '|_', kam[0], '=', kam[1])
                                                    else:
                                                        siam = len(eval(kam[1].name).__dict__.items())
                                                        sdaf = eval(kam[1].name).__dict__
                                                        tiersdaf = eval(sdaf['name']).tier
                                                        if siam == 1:
                                                            print("\t\t\t\t", "|_", 'name' + ':', sdaf['name'], tiersdaf)
                                                        
