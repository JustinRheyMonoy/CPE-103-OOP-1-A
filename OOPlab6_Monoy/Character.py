class Character():
    def __init__(self, username):
        self.__username = username
        self.__hp = 100
        self.__mana = 100
        self.__damage = 5
        self.__str = 0  # strength stat
        self.__vit = 0  # vitality stat
        self.__int = 0  # intelligence stat
        self.__agi = 0  # agility stat

    def getUsername(self):
        return self.__username

    def setUsername(self, new_username):
        self.__username = new_username

    def getHp(self):
        return self.__hp

    def setHp(self, new_hp):
        self.__hp = max(0,new_hp)

    def getDamage(self):
        return self.__damage

    def setDamage(self, new_damage):
        self.__damage = max(0, new_damage)

    def getStr(self): 
        return self.__str
    
    def setStr(self, new_str): self.__str = max(0, new_str)

    def getVit(self): 
        return self.__vit
    
    def setVit(self, new_vit): self.__vit = max(0, new_vit)

    def getInt(self): 
        return self.__int
    
    def setInt(self, new_int): self.__int = max(0, new_int)

    def getAgi(self): 
        return self.__agi
    
    def setAgi(self, new_agi): self.__agi = max(0, new_agi)
    
    def reduceHp(self, damage_amount):
        self.__hp = max(0, self.__hp - damage_amount)

    def addHp(self, heal_amount):
        self.__hp = min(100, self.__hp + heal_amount)
        

#character1 = Character("UnExpected:)") 
#print(character1.getUsername())

    
