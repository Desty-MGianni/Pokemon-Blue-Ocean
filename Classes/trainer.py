import random
import math
import beaupy
from time import sleep
from Classes.inventory import Inventory
from Classes.pokemon import Pokémon
from Classes.clearscreen import clearscreen

class Trainer:
    
    # in prevision of save game feature
    #list_trainer_obj: dict[str: bool] = {}

            
    def __init__(self,name:str ,list_pokémon:list[Pokémon]) -> None:
        self.name = name
        self.is_player = False
        self.list_pokémon = list_pokémon
        self.has_lost_vs_player = False
        
        # in prevision of save game feature
        #Trainer.list_trainer_obj.update({self.name: self.has_lost_vs_player})

    def __str__(self) -> str:
        str_output = f"\nTrainer: \n\t{self.name} \n"
        str_output += "Pokémon list:"
        counter = 1
        for pokémon in self.list_pokémon:
            str_output += f"\n\t{counter}|{pokémon}"
            counter += 1
        return str_output
            
    # method that verify if every pokémon of the trainer are K.O.
    def check_all_pok_ko(self) -> bool:
        counter = 0
        for pokémon in self.list_pokémon:
            if pokémon.is_ko:
                counter += 1
        if counter == len(self.list_pokémon):
            self.lose_update()
            return True
        else:
            return False
    
    def lose_update(self) -> None:
        self.has_lost_vs_player = True
        #Trainer.list_trainer_obj[self.name] = True
    
    # it cycle in the list of pokémon, there is no "swap" available for trainers
    def change_pokemon(self) -> None:
        temp = self.list_pokémon[0]
        self.list_pokémon.pop(0)
        self.list_pokémon.append(temp)
        sleep(1)
        print(f"{self.list_pokémon[0].name}, Go!")

class Player(Trainer):

    def __init__(self, name:str, list_pokémon: list[Pokémon]) -> None:
        super().__init__(name, list_pokémon)
        self.is_player = True
        self.inventory = Inventory()
    
    def __str__(self) -> str:
        var_for_badges: dict[str: int] = self.inventory.get_badges()
        str_output: str = "Badges:"
        for badge in var_for_badges:
            str_output += f"\n\t{badge}"
        return super().__str__() + \
        f"\n{str_output}" \
        f"\n{str(self.inventory)}"
    
    # Logic for capturing pokémon, called in use_item method
    def __capture_pokemon(self, wild_pokemon: Pokémon, odds_from_poké_ball: int) -> None:
        odds: int = odds_from_poké_ball
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
        success_number: int = random.randint(1,100)
        print("\t.")
        sleep(1)
        print("\t.")
        sleep(1)
        print("\t.")
        sleep(0.5)
        if success_number <= odds:
            print(F"Congratulation, {wild_pokemon.name} has been captured!")
            sleep(1)
            wild_pokemon.is_wild = False
            if beaupy.confirm(f"Do you want to change the name of {wild_pokemon.name} ?"):
                wild_pokemon.change_name()
            self.__check_limit_list_pokemon(wild_pokemon)
        else:
            print("Oh no, he freed himself!")

    # Method that will check if we can put the captured pokémon in the pokémon_list or PC if the list is too big!.                                                                                                        
    def __check_limit_list_pokemon(self,wild_pokemon: Pokémon) -> None:
        if len(self.list_pokémon) == 6:
            print("You already have the maximum amount of pokémon with you!")
            sleep(1)
            self.inventory.add_pok_pc(wild_pokemon)
            print(f"{wild_pokemon.name} is sent to the PC!")
            sleep(1)
        else: 
            self.list_pokémon.append(wild_pokemon) 
    
    # method that is called in battle.py to swap the first pokémon. We return a bool so that, 
    # in battle method, we advance in the turn or not.
    def change_pokemon(self) -> bool:
        print("\tSelect Pokémon:")
        choice: int = beaupy.select(
            options= self.list_pokémon + ['Cancel'],
            return_index= True,
            cursor= "--->"
        )
        if choice == 0:
            return False
        # as lenght is 1 unit higher as indexes, with this, we can access "Cancel"
        elif choice == len(self.list_pokémon):
            return False

        temp: Pokémon = self.list_pokémon[0]
        self.list_pokémon[0] = self.list_pokémon[choice]
        self.list_pokémon[choice] = temp
        sleep(1)
        del temp
        print(f"{self.list_pokémon[0].name}, Go!")
        return True
    
    # is called in menu and battle. The bool return type is used for battle method so that depending what we have done we advance in the turn or not.
    def use_item(
            self, 
            in_battle_vs_trainer: bool = False, 
            in_battle_vs_wild_pok: bool = False, 
            wild_pokémon: Pokémon = None
        ) -> bool:
        
        if in_battle_vs_trainer and in_battle_vs_wild_pok:
            print("Error! You can't be in a battle vs a trainer AND a wild Pokémon!")
            return False
        clearscreen()
        self.inventory.update_items_available()
        print("Category of items:")
        cat_to_use: list[str] = ["Poké Balls", "Potions and Revives", "Evolution Stones"]
        choice_cat: str = beaupy.select(
            options= cat_to_use,
            return_index= False,
            cursor= "--->"
        )
        match choice_cat:

            case "Poké Balls":
                if not in_battle_vs_trainer and not in_battle_vs_wild_pok:
                    print("You need to be in battle to use a Poké Ball!")
                    sleep(1)
                    return False
                elif in_battle_vs_trainer:
                    print(f"You can't capture a pokémon that's already been captured by another trainer!")
                    sleep(1)
                    return False
                elif in_battle_vs_wild_pok:
                    if self.list_pokémon[0].is_ko:
                        print("You can't use a pokéball when your pokémon is KO!")
                        sleep(1)
                        return False
                    else:
                        # Need to execute this step as beaupy.select don't handle dict data type
                        options: list[str] = list(self.inventory.balls_available.keys()) 
                        
                        print("Select the ball")
                        choice_ball: str = beaupy.select(
                            options,
                            preprocessor= lambda x: f"{x} x {self.inventory.balls_available[x]}",
                            return_index= False,
                            cursor= "--->"
                        )
                        if choice_ball != None:
                            odds: int = 0
                            odds += self.inventory.use_ball(object_name= choice_ball)
                            self.__capture_pokemon(wild_pokemon= wild_pokémon,odds_from_poké_ball= odds)
                            return True
                        else:
                            input("You don't have any Poké Balls available!")
                            sleep(1)
                            return False
            
            case "Potions and Revives":
                
                # Need to execute stis line becauase beaupy don't hande dict data type
                options: list[str]= list(self.inventory.potions_available.keys()) + (list(self.inventory.revives_available.keys()))
                
                print("\tPotions and Revives:")
                choice_heal: str = beaupy.select(
                    options,
                    preprocessor= lambda x: f"{x} x {self.inventory.potions_available[x]}" if x in self.inventory.potions else f"{x} x {self.inventory.revives_available[x]}",
                    return_index= False,
                    cursor= "--->"
                )
                if choice_heal != None:
                    print(f"which Pokémon do you want to use {choice_heal}?")
                    choice_pok_heal: int = beaupy.select(
                        options= self.list_pokémon,
                        preprocessor= lambda x : 
                        f"{x.name}: K.O"if x.is_ko else f"{x.name}: {x.health}/{x.max_health}",
                        return_index= True,
                        cursor= "--->"
                    )
                    if choice_heal in self.inventory.potions_available:
                        self.inventory.use_potion(object_name= choice_heal, pokémon= self.list_pokémon[choice_pok_heal])
                        sleep(1)
                        return True
                    elif choice_heal in self.inventory.revives_available:
                        self.inventory.use_revive(object_name= choice_heal, pokémon= self.list_pokémon[choice_pok_heal])
                        sleep(1)
                        return True
                    else:
                        return False
                else:
                    input("You don't have any potion or revives available!")
                    sleep(1)
                    return False
       
            case "Evolution Stones":
                if not in_battle_vs_trainer and not in_battle_vs_wild_pok:
                    
                    # Need to execute this line because beaupy don't handle dict data type.
                    options: list[str] = list(self.inventory.stones_available.keys())

                    print("Select the stone you want to use:")
                    choice_evo_stone: str = beaupy.select(
                        options,
                        preprocessor= lambda x: f"{x} x {self.inventory.balls_available[x]}",
                        return_index= False,
                        cursor= "--->"
                    )
                    if choice_evo_stone != None:
                        pokemon_to_stone_evolve: int = beaupy.select(
                            options= self.list_pokémon,
                            preprocessor= lambda x: f"{x.name}: YES" if x.check_stone_evolution(stone= choice_evo_stone) else f"{x.name}: NO", 
                            return_index= True, 
                            cursor= "--->"
                        )
                        if pokemon_to_stone_evolve != None and self.list_pokémon[pokemon_to_stone_evolve].check_stone_evolution(stone= choice_evo_stone):
                            if self.inventory.use_stone(stone= choice_evo_stone, pokémon= self.list_pokémon[pokemon_to_stone_evolve]):
                                return True
                        return False
                    else:
                        input("You don't have any evolution stone available!")
                        sleep(1)
                        return False
                else:
                    print("You can't use an evolution stones in a battle!")
                    sleep(1)
                    return False

            