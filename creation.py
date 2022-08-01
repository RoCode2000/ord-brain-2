# Hidden Random Unit
class HiddenRandom:
    tier = "'Luck'"
    def __init__(self, name):
        self.name = name

    # def __str__(self) -> str:
    #     return f"{self.name} {self.tier}"

    def base(self):
        return f"{self.name} {self.tier}"
# Common
class Common:
    tier = "'C'"

    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return f"{self.name} {self.tier}"

    def base(self):
        return f"{self.name} {self.tier}"
# Uncommon
class Uncommon():
    tier = "'U'"

    def __init__(self, name, material1, material2):
        self.name = name
        self.material1 = material1
        self.material2 = material2

    # def __str__(self):
    #     return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2}"

    def base(self):
        return f"{self.name} {self.tier}, {self.material1} {self.material2}"
# Special
class Special():
    tier = "'S'"

    def __init__(self, name, material1, material2, material3):
        self.name = name
        self.material1 = material1
        self.material2 = material2
        self.material3 = material3

    # def __str__(self):
    #     return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3}"

    def base(self):
        return f"{self.name} {self.tier}, {self.material1} {self.material2} {self.material3}"
class SpecialDoubleClass():
    tier = "'S'"

    def __init__(self, name, material1, material2):
        self.name = name
        self.material1 = material1
        self.material2 = material2

    # def __str__(self) -> str:
    #     return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2}"

    def base(self):
        return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2}"
class SpecialQuadClass():
    tier = "'S'"

    def __init__(self, name, material1, material2, material3, material4):
        self.name = name
        self.material1 = material1
        self.material2 = material2
        self.material3 = material3
        self.material4 = material4

    # def __str__(self) -> str:
    #     return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3} \n{self.material4}"

    def base(self):
        return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3} \n{self.material4}"
# Rare
class Rare():
    tier = "'R'"

    def __init__(self, name, material1, material2, material3):
        self.name = name
        self.material1 = material1
        self.material2 = material2
        self.material3 = material3

    # def __str__(self):
    #     return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3}"

    def base(self):
        return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3}"
class RareQuadClass():
    tier = "'R'"

    def __init__(self, name, material1, material2, material3, material4):
        self.name = name
        self.material1 = material1
        self.material2 = material2
        self.material3 = material3
        self.material4 = material4

    # def __str__(self):
    #     return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3} \n{self.material4}"

    def base(self):
        return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3} \n{self.material4}"
class RarePenClass():
    tier = "'R'"

    def __init__(self, name, material1, material2, material3, material4, material5):
        self.name = name
        self.material1 = material1
        self.material2 = material2
        self.material3 = material3
        self.material4 = material4
        self.material5 = material5

    # def __str__(self):
    #     return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3} \n{self.material4} \n{self.material5}"

    def base(self):
        return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3} \n{self.material4} \n{self.material5}"
# Legendary
class Legendary(Rare):
    tier = "'L'"

    def __init__(self, name, material1, material2, material3):
        super().__init__(name, material1, material2, material3)

    # def __str__(self):
    #     return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3}"

    def base(self):
        return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3}"
class LegendaryQuad():
    tier = "'L'"

    def __init__(self, name, material1, material2, material3, material4):
        self.name = name
        self.material1 = material1
        self.material2 = material2
        self.material3 = material3
        self.material4 = material4

    # def __str__(self) -> str:
    #     return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3} \n{self.material4}"

    def base(self):
        return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3} \n{self.material4}"
# Immortal
class Immortal():
    tier = "'I'"

    def __init__(self, name, material1, material2, material3):
        self.name = name
        self.material1 = material1
        self.material2 = material2
        self.material3 = material3

    # def __str__(self) -> str:
    #     return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3}"

    def base(self):
        return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3}"
# Hidden
class HiddenTriple():
    tier = "'H'"

    def __init__(self, name, material1, material2, material3):
        self.name = name
        self.material1 = material1
        self.material2 = material2
        self.material3 = material3

    # def __str__(self) -> str:
    #     return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3}"

    def base(self):
        return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3}"
class HiddenQuad():
    tier = "'H'"

    def __init__(self, name, material1, material2, material3, material4):
        self.name = name
        self.material1 = material1
        self.material2 = material2
        self.material3 = material3
        self.material4 = material4

    # def __str__(self) -> str:
    #     return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3} \n{self.material4}"

    def base(self):
        return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3} \n{self.material4}"
class HiddenPen():
    tier = "'H'"

    def __init__(self, name, material1, material2, material3, material4, material5):
        self.name = name
        self.material1 = material1
        self.material2 = material2
        self.material3 = material3
        self.material4 = material4
        self.material5 = material5

    # def __str__(self) -> str:
    #     return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3} \n{self.material4} \n{self.material5}"

    def base(self):
        return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3} \n{self.material4} \n{self.material5}"
# Alternate Unit
class Alternate:
    tier = "'A'"
    def __init__(self, name, material1):
        self.name = name
        self.material1 = material1

    # def __str__(self) -> str:
    #     return f"{self.name} {self.tier}"

    def base(self):
        return f"{self.name} {self.tier}, \n{self.material1} "
# Transcended
class TranscendedQuad:
    def __init__(self, name, material1, material2, material3, material4):
        self.name = name
        self.material1 = material1
        self.material2 = material2
        self.material3 = material3
        self.material4 = material4

    def base(self):
        return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3} \n{self.material4}"
class TranscendedPen:
    def __init__(self, name, material1, material2, material3, material4, material5):
        self.name = name
        self.material1 = material1
        self.material2 = material2
        self.material3 = material3
        self.material4 = material4
        self.material5 = material5

    def base(self):
        return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3} \n{self.material4} \n{self.material5}"
class TranscendedHex:
    def __init__(self, name, material1, material2, material3, material4, material5, material6):
        self.name = name
        self.material1 = material1
        self.material2 = material2
        self.material3 = material3
        self.material4 = material4
        self.material5 = material5
        self.material6 = material6

    def base(self):
        return f"{self.name} {self.tier}, \n{self.material1} \n{self.material2} \n{self.material3} \n{self.material4} \n{self.material5} \n{self.material6}"