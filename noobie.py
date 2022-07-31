import re
from readline import write_history_file
from tkinter import N

from common.unit import *
from uncommon.unit import *
from special.unit import *
from rare.unit import *
from legendary.unit import *
from immortal.unit import *
from hidden.unit import *

# luffy_amt = int(input("How many Luffy: "))
# zoro_amt = int(input("How many Zoro: "))
# nami_amt = int(input("How many Nami: "))
# usopp_amt = int(input("How many Usopp: "))
# sanji_amt = int(input("How many Sanji: "))
# chopper_amt = int(input("How many Chopper: "))
# buggy_amt = int(input("How many Buggy: "))
# gunman_amt = int(input("How many Gunman: "))
# swordsman_amt = int(input("How many Swordsman: "))

# have_char = [luffy_amt, zoro_amt, nami_amt, usopp_amt, sanji_amt, chopper_amt, buggy_amt, gunman_amt, swordsman_amt]

r = killer_hidden
ro = r.__dict__
# print(capone_special.__dict__)
# ro = r.base()
# gro = eval(r).name
# print(gro)

# print(ro)

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
            # print(n.items())
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
                                                        
                                             
                            
            



common_characters = ["Luffy 'C'", "Zoro 'C'", "Nami 'C'", "Usopp 'C'", "Sanji 'C'", "Chopper 'C'", "Buggy 'C'", "Gunman 'C'", "Swordsman 'C'"]
uncommon_characters = []
special_characters = []
rare_characters = []
legendary_characters = []
hidden_characters = []

# print("<------->")
# print(ro)
# print("<------->")

# with open("./uncommon/unit.py", "r") as file:
#     x = file.read()
#     y = re.findall("\w*\s=\s[A-Z]", x)
#     for m in y:
#         uppergod = m[:-4]
#         easylah = eval(uppergod).name
#         tierlah = eval(uppergod).tier
#         new_append = easylah + " " + tierlah
#         uncommon_characters.append(new_append)
#     file.close()

# with open("./special/unit.py", "r") as file:
#     x = file.read()
#     y = re.findall("\w*\s=\s[A-Z]", x)
#     for m in y:
#         uppergod = m[:-4]
#         easylah = eval(uppergod).name
#         tierlah = eval(uppergod).tier
#         new_append = easylah + " " + tierlah
#         special_characters.append(new_append)
#     file.close()

# with open("./rare/unit.py", "r") as file:
#     x = file.read()
#     y = re.findall("\w*\s=\s[A-Z]", x)
#     for m in y:
#         uppergod = m[:-4]
#         easylah = eval(uppergod).name
#         tierlah = eval(uppergod).tier
#         new_append = easylah + " " + tierlah
#         rare_characters.append(new_append)
#     file.close()

# with open("./legendary/unit.py", "r") as file:
#     x = file.read()
#     y = re.findall("\w*\s=\s[A-Z]", x)
#     for m in y:
#         uppergod = m[:-4]
#         easylah = eval(uppergod).name
#         tierlah = eval(uppergod).tier
#         new_append = easylah + " " + tierlah
#         legendary_characters.append(new_append)
#     file.close()

# with open("./hidden/unit.py", "r") as file:
#     x = file.read()
#     y = re.findall("\w*\s=\s[A-Z]", x)
#     for m in y:
#         uppergod = m[:-4]
#         easylah = eval(uppergod).name
#         tierlah = eval(uppergod).tier
#         new_append = easylah + " " + tierlah
#         hidden_characters.append(new_append)
#     file.close()


# for cochar in common_characters:
#     x = re.findall(cochar, ro)
#     if x != []:
#         print(len(x), cochar)
# print("---------")


# for unchar in uncommon_characters:
#     x = re.findall(unchar, ro)
#     if x != []:
#         print(len(x), unchar)
# print("---------")


# for spchar in special_characters:
#     x = re.findall(spchar, ro)
#     if x != []:
#         print(len(x), spchar)
# print("---------")


# for rachar in rare_characters:
#     x = re.findall(rachar, ro)
#     if x != []:
#         print(len(x), rachar)
# print("---------")


# for lechar in legendary_characters:
#     x = re.findall(lechar, ro)
#     if x != []:
#         print(len(x), lechar)
# print("---------")

# for hichar in hidden_characters:
#     x = re.findall(hichar, ro)
#     if x != []:
#         print(len(x), hichar)
# print("---------")


## Write Building Material
# with open ("./immortal/unit.py", "r") as file:
#     x = file.read()
#     y = re.findall("\w*\s=\s[A-Z]", x)
#     q = y
#     for m in q:
#         god = m[:-4]
#         w = eval(god)
#         woohoo = w.base()
#         namewoohoo = w.name
#         tierwoohoo = w.tier
#         with open ("./immortal/crafting.txt", "a") as newfile:
#             newfile.write("<-----------")
#             newfile.write(namewoohoo)
#             newfile.write("---")
#             newfile.write(tierwoohoo)
#             newfile.write("----------->\n")
#             for char in common_characters:
#                 x = re.findall(char, woohoo)
#                 if x != []:
#                     newoutput = str(len(x)) + "\t" + char
#                     newfile.write(newoutput)
#                 else:
#                     newfile.write("Not Found")
#                 newfile.write("\n")
#             newfile.close()

#     file.close()

