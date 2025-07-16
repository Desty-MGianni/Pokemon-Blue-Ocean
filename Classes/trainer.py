import random
import math
from time import sleep
from Classes import inventory
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
    def __init__(self,name:str ,list_pokémon:list):
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

    def __init__(self, name:str, list_pokémon: list):
        super().__init__(name, list_pokémon)
        self.is_player = True
        self.inventory = Inventory()
    
    def __repr__(self):
        return super().__repr__() + f"\n{str(self.inventory)}"
    
    # method that will capture wild pokémon when call in inventory function.
    def __capture_pokemon(self, wild_pokemon: Pokémon, odds_from_poké_ball: int):
        odds = odds_from_poké_ball
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
            self.__check_limit_list_pokemon(wild_pokemon)
        else:
            print("Oh no, he freed himself!")

    # Method that will check if we can put the captured pokémon in the pokémon_list or PC if the list is too big!.                                                                                                        
    def __check_limit_list_pokemon(self,wild_pokemon: Pokémon):
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
    
    def use_item(self, in_battle_vs_trainer: bool = False, in_battle_vs_wild_pok: bool = False, wild_pokémon: Pokémon = None):
        
        if in_battle_vs_trainer and in_battle_vs_wild_pok:
            print("Error! You can't be in a battle vs a trainer AND a wild Pokémon!")
            return False
        
        print(self.inventory)
        item = input("Enter the item you want ot use: ").title()
        print(item)

        if item in self.inventory.balls:
            if not in_battle_vs_trainer and not in_battle_vs_wild_pok:
                print("It is useless to use a Poké Ball outside a battle versus a Pokémon!")
                return False
            elif in_battle_vs_trainer:
                print(f"You can't capture a pokémon that's already been captured by another trainer!")
                return False
            elif in_battle_vs_wild_pok:
                if self.list_pokémon[0].is_ko:
                    print("You can't use a pokéball when your pokémon is KO!")
                    return False
                else:
                    if self.inventory.verify_quantity_in_dict(object_name= item, dict_looked= self.inventory.balls):
                        odds = 0
                        odds += self.inventory.use_ball(object_name= item)
                        self.__capture_pokemon(wild_pokemon= wild_pokémon,odds_from_poké_ball= odds)
                        return True
                    else:
                        print(f"You don't have any {item}")
                        return False
                    
        elif item in self.inventory.potions or item in self.inventory.revives:
            while True:
                print(f"which Pokémon do you want to use {item}? (Enter the index of the Pokémon. Every other input will cancel.)")
                counter = 1
                for pokémon in self.list_pokémon:
                    print(f"\t{counter}: K.O = {pokémon.is_ko}|{pokémon}")
                try:
                    answer = int(input())
                except ValueError:
                    answer = -1

                if answer >=1 and answer <= len(self.list_pokémon):
                    if item in self.inventory.potions and self.inventory.verify_quantity_in_dict(object_name= item, dict_looked= self.inventory.potions) and self.inventory.use_potion(object_name= item, pokémon= self.list_pokémon[answer -1]):
                        return True
                    elif item in self.inventory.revives and self.inventory.verify_quantity_in_dict(object_name= item, dict_looked= self.inventory.revives) and self.inventory.use_revive(object_name= item, pokémon= self.list_pokémon[answer -1]):
                        return True
                    else:
                        return False
        
        elif item in self.inventory.stones:
            if not in_battle_vs_trainer and not in_battle_vs_wild_pok:
                for pokémon in self.list_pokémon:
                    if self.inventory.verify_quantity_in_dict(object_name= item, dict_looked= self.inventory.stones):
                        if self.inventory.use_stone(object_name= item, pokémon= pokémon):
                            pass
                        else:
                            continue
                    else:
                        print(F"You don't have any {item}")
                        return False
            else:
                print("You can't use an evolution stones in a battle!")
                return False
            return True
            
        elif item == "Cancel":
            return False
        
        else:
            print("Invalid")