import random
import math
from time import sleep
from Classes.inventory import Inventory
from Classes.pokemon import Pokémon

class Trainer:
    def __repr__(self):
        str_output = f"\nTrainer: \n\t{self.name} \n"
        str_output += "Pokémon list:"
        counter = 1
        for pokémon in self.list_pokémon:
            str_output += f"\n\t{counter}|{pokémon}"
            counter += 1
        return str_output
            
    # Constructor
    def __init__(self,name,list_pokémon:list):
        self.name = name
        self.is_player = False
        self.list_pokémon = list_pokémon
            
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
    
    def change_pokemon(self):
        temp = self.list_pokémon[0]
        self.list_pokémon.pop(0)
        self.list_pokémon.append(temp)
        sleep(1)
        print(f"{self.list_pokémon[0].name}, Go!")

class Player(Trainer):

    def __init__(self, name, list_pokémon):
        super().__init__(name, list_pokémon)
        self.is_player = True
        self.inventory = Inventory()
    
    def __repr__(self):
        return super().__repr__() + f"\n{str(self.inventory)}"
    
    # method that will capture wild pokémon when call in inventory function.
    def capture_pokemon(self, wild_pokemon: Pokémon, odds: int):
        match wild_pokemon.health:
            case _ if wild_pokemon.health <= math.ceil(wild_pokemon.max_health * 0.1):
                odds+= 30
            case _ if wild_pokemon.health <= math.ceil(wild_pokemon.max_health * 0.2):
                odds+= 25
            case _ if wild_pokemon.health <= math.ceil(wild_pokemon.max_health * 0.3):
                odds+= 20
            case _ if wild_pokemon.health <= math.ceil(wild_pokemon.max_health * 0.4):
                odds += 15
            case _ if wild_pokemon.health <= math.ceil(wild_pokemon.max_health * 0.5):
                odds += 10
            case _ if wild_pokemon.health <= math.ceil(wild_pokemon.max_health * 0.6):
                odds += 5
        success_number = random.randint(1,100)
        print(odds)
        print("\t.")
        sleep(1)
        print("\t.")
        sleep(1)
        print("\t.")
        sleep(0.5)
        if success_number <= odds:
            print(F"Congratulation, {wild_pokemon.name} has been captured!")
            wild_pokemon.is_wild = False
            self.check_limit_pokemon(wild_pokemon)
        else:
            print("Oh no, he freed himself!")

    # Method that will check if we can put the captured pokémon in the pokémon_list or PC if the list is too big!.                                                                                                        
    def check_limit_pokemon(self,wild_pokemon: Pokémon):
        if len(self.list_pokémon) == 6:
            print("You already have the maximum amount of pokémon with you!")
            sleep(1)
            self.inventory.add_pok_pc(wild_pokemon)
            print(f"{wild_pokemon.name} is sent to the PC!")
        else: 
            self.list_pokémon.append(wild_pokemon) 
    def change_pokemon(self):
        print("Enter the number corresponding to the pokémon: ")
        counter = 1
        for pokemon in self.list_pokémon:
            print(f"{counter} {pokemon}")
            counter += 1
        choice = int(input())
        temp = self.list_pokémon[0]
        self.list_pokémon[0] = self.list_pokémon[choice - 1]
        self.list_pokémon[choice - 1] = temp
        sleep(1)
        print(f"{self.list_pokémon[0].name}, Go!")
    

