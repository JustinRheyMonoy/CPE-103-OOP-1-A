import random
from Novice import Novice
from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Boss import Boss

def select_character(player_name, allow_boss=False):
    """Allows the player to select a character class."""
    roles = {"1": Novice, "2": Swordsman, "3": Archer, "4": Magician}
    if allow_boss:
        roles["5"] = Boss
    
    while True:
        print("Select a class:")
        for key, role in roles.items():
            print(f"{key}: {role.__name__}")
        choice = input("Enter choice: ")
        if choice in roles:
            return roles[choice](player_name)
        print("Invalid choice. Try again.")

def take_turn(player, opponent):
    """Handles turn-based combat for the game."""
    actions = ["Basic Attack", "Slash Attack", "Ranged Attack", "Magic Attack", "Heal"]
    
    print(f"{player.getUsername()}'s turn!")
    print("Select an action:")
    for i, action in enumerate(actions, 1):
        print(f"{i}: {action}")
    
    choice = input("Enter choice: ")
    if choice == "1":
        player.basicAttack(opponent)
    elif choice == "2" and hasattr(player, 'slashAttack'):
        player.slashAttack(opponent)
    elif choice == "3" and hasattr(player, 'rangedAttack'):
        player.rangedAttack(opponent)
    elif choice == "4" and hasattr(player, 'magicAttack'):
        player.magicAttack(opponent)
    elif choice == "5" and hasattr(player, 'heal'):
        player.heal()
    else:
        print("Invalid action! Skipping turn.")

def play_game():
    """Main game loop for single-player or player vs player mode."""
    print("Welcome to the Game!")
    wins = {"Player": 0, "Monster": 0}
    mode = input("Select mode: 1 for Single Player, 2 for PvP: ")
    
    if mode == "1":
        player = select_character("Player")
        opponent = Boss("Monster")
    else:
        player1 = select_character("Player 1")
        player2 = select_character("Player 2")
    
    while True:
        if mode == "1":
            players = [player, opponent]
        else:
            players = [player1, player2]
        
        random.shuffle(players)
        
        for p in players:
            if mode == "1":
                take_turn(p, opponent if p == player else player)
            else:
                take_turn(p, player2 if p == player1 else player1)
            
            if player.getHp() <= 0:
                print("Monster wins!")
                wins["Monster"] += 1
                break
            elif opponent.getHp() <= 0:
                print("Player wins!")
                wins["Player"] += 1
                break
        
        print(f"Scores - Player: {wins['Player']}, Monster: {wins['Monster']}")
        
        if mode == "1" and wins["Player"] >= 2:
            print("You've won 2 times! Choose a new class.")
            player = select_character("Player")
        
        if input("Play again? (y/n): ").lower() != "y":
            break
    
if __name__ == "__main__":
    play_game()
