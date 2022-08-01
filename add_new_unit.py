# Inquire whether there is new unit
def new_unit():
    while True:
        new_unit = input("Is there a new unit(y/n): ").lower()

        if new_unit == "y" or new_unit == "n":
            break

        print("Please input either y or n!\n")
    
    # Inquire tier of new unit
    if new_unit == "y":
        while True:
            tier_of_unit = input("What is the tier of the new unit(c,u,s,r,l,i,h,a,t): ").lower()

            if tier_of_unit == "c" or tier_of_unit == "u" or tier_of_unit == "s" or tier_of_unit == "r" or tier_of_unit == "l" or tier_of_unit == "i" or tier_of_unit == "h" or tier_of_unit == "a" or tier_of_unit == "t":
                break
    
        return f"{tier_of_unit}"
    else:
        return None

# Ask for tier of unit
tier_of_unit = new_unit()

if tier_of_unit != None:
    # Check for number of new unit
    number_of_new_unit = int(input("How many new unit of do you want to add: "))

# Add Unit
if tier_of_unit == "c":
    for x in range(number_of_new_unit):
        unit = input("Input unit such as (luffy_common): ").lower()

        with open ("./common/unit.py", "a") as file:
            file.write("{} = Common('{}')\n".format(unit, unit))
            file.close()
elif tier_of_unit == "u":
    for x in range(number_of_new_unit):
        unit = input("Input unit such as (luffy_uncommon): ").lower()

        with open ("./uncommon/unit.py", "a") as file:
            file.write("{} = Uncommon('{}',)\n".format(unit, unit))
            file.close()
elif tier_of_unit == "s":
    for x in range(number_of_new_unit):
        unit = input("Input unit such as (luffy_special): ").lower()

        with open ("./special/unit.py", "a") as file:
            file.write("{} = Special('{}',)\n".format(unit, unit))
            file.close()
elif tier_of_unit == "r":
    for x in range(number_of_new_unit):
        unit = input("Input unit such as (luffy_rare): ").lower()

        with open ("./rare/unit.py", "a") as file:
            file.write("{} = Rare('{}',)\n".format(unit, unit))
            file.close()
elif tier_of_unit == "l":
    for x in range(number_of_new_unit):
        unit = input("Input unit such as (luffy_legendary): ").lower()

        with open ("./legendary/unit.py", "a") as file:
            file.write("{} = Legendary('{}',)\n".format(unit, unit))
            file.close()
elif tier_of_unit == "i":
    for x in range(number_of_new_unit):
        unit = input("Input unit such as (luffy_immortal): ").lower()

        with open ("./immortal/unit.py", "a") as file:
            file.write("{} = Immortal('{}',)\n".format(unit, unit))
            file.close()
elif tier_of_unit == "h":
    ## Must change base one number of base
    for x in range(number_of_new_unit):
        unit = input("Input unit such as (luffy_hidden): ").lower()

        with open ("./hidden/unit.py", "a") as file:
            file.write("{} = Hidden('{}',)\n".format(unit, unit))
            file.close()
elif tier_of_unit == "a":
    for x in range(number_of_new_unit):
        unit = input("Input unit such as (luffy_alternate): ").lower()

        with open ("./alternate/unit.py", "a") as file:
            file.write("{} = Alternate('{}',)\n".format(unit, unit))
            file.close()
elif tier_of_unit == "t":
    ## Must change base one number of base
    for x in range(number_of_new_unit):
        unit = input("Input unit such as (luffy_transcended): ").lower()

        with open ("./transcended/unit.py", "a") as file:
            file.write("{} = Transcended('{}',)\n".format(unit, unit))
            file.close()