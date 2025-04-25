from Novice import Novice
import random

class Archer(Novice):
    def __init__(self, username):
        super().__init__(username)
        self.setAgi(5)
        self.setInt(5)
        self.setVit(5)
        self.setHp(self.getHp()+self.getVit())
        self.new_damage = 0
        
    def rangedAttack(self, character):
        new_damage = self.getDamage() + random.randint(1, self.getInt())
        character.reduceHp(new_damage)
        print(f"{self.getUsername()} performed Ranged Attack! -{new_damage}")
    