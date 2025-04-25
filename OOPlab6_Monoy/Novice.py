from Character import Character

class Novice(Character):
    def __init__(self, username):
        super().__init__(username)
        
    def basicAttack(self, character):
        character.reduceHp(self.getDamage())
        print(f"{self.getUsername()} performed Basic Attack! -{self.getDamage()}")
        
# Creating an instance of Novice, which inherits from Character
#character1 = Novice("UnExpected:)")

# Using the getter method to print the username
#print(character1.getUsername()) # Expected output: "UnExpected:)"

# Using the getter method to print HP
#print(character1.getHp()) # Expected output: 100