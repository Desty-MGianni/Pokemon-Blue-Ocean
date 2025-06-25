import random
from Classes import inventory as i

class Trainer:
    # Constructor
    def __init__(self,name,list_pokémon:list):
        self.name = name
        self.is_player = False
        self.list_pokémon = list_pokémon
        self.money = random.randint(750,3250)
        self.badge = 0
    
    # toggle method that set a trainer as the player
    def create_player(self):
        self.is_player = True
        self.money = 3000
        self.inventory = i.Inventory()
        
    # method that verify if every pokémon of the trainer are K.O.
    def check_all_pok_ko(self):
        counter = 0
        for pokémon in self.list_pokémon:
            if pokémon.is_ko:
                counter += 1
        if counter == len(self.list_pokémon):
            return True
        else:
            return False
    









