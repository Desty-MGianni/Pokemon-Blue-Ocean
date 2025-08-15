from Classes.battle import battle
from Classes.menu import menu
from Classes.trainer import Trainer, Player
from Classes.clearscreen import clearscreen
from Classes.pokemon import Pokémon
from time import sleep
import random


class Road:
    def __init__(self, name: str,list_wild_pok_id: list, wild_pok_lvl_range: range, list_trainers: list):
        self.name = name
        self.trainers = list_trainers
        self.wild_pok_id_available = list_wild_pok_id
        self.wild_pok_level_range = wild_pok_lvl_range
        self.has_beaten_all_trainer = False

    def roaming(self, player: Player):
        if self.name == "Route 22" and player.inventory.has_all_badges():
            print("You have to prove that you can challenge the league!")
            sleep(2)
            battle(
                player= player, 
                opponent= Trainer(
                    name= "Rival",
                    list_pokémon= [
                        Pokémon(pok_id= 18, level= 47),
                        Pokémon(pok_id= 65, level= 47),
                        Pokémon(pok_id= 111, level= 45),
                        Pokémon(pok_id= 59, level= 45),
                        Pokémon(pok_id= 130, level= 45),
                        Pokémon(pok_id= 3, level= 53)
                    ]
                ))
        while True:
            print(self.name)
            choice =input("What do you want to do ?:\n" \
            "\t1| Go through the road (you will battle vs trainers if not already done.)\n" \
            "\t2| Roam through the bushes\n" \
            "\tM| Open menu\n" \
            "\tE| Exit the road\n")
        
            if choice == 'e' or choice == 'E':
                break
            elif choice == 'm' or choice == 'M':
                menu(player= player)
                continue
            try:
                choice_int = int(choice)
            except ValueError:
                choice_int = 0
            match choice_int:
                case 0:
                    print("incorrect input, please enter a number!")
                case 1:
                    clearscreen()
                    if self.trainers == None:
                        print("There is no traniers in this road!")
                        sleep(1)
                        clearscreen()
                    else:
                        trainers_index = 0
                        if trainers_index >= 0 and trainers_index < len(self.trainers):
                            battle(player= player, opponent= self.trainers[trainers_index])
                            if self.trainers[trainers_index].has_lost_vs_player:
                                trainers_index += 1
                        else:
                            if not self.has_beaten_all_trainer:
                                self.has_beaten_all_trainer = True
                            else:
                                print("You have already beaten all the trainers on this road!")
                                sleep(1)
                                clearscreen()
                case 2:
                    sleep(1)
                    clearscreen()
                    pok_index = random.randint(0, len(self.wild_pok_id_available) - 1)
                    pok_level = random.randint(0, len(self.wild_pok_level_range) - 1)
                    if random.randint(0,100) <= 50:
                        battle(
                            player= player, 
                            opponent= Pokémon(
                                pok_id= self.wild_pok_id_available[pok_index],
                                is_wild= True, 
                                level= self.wild_pok_level_range[pok_level]
                            )
                        )
                case _:
                    clearscreen()
                    pass

class Site(Road):
    def __init__(self, name: str, list_wild_pok_id: list, wild_pok_lvl_range: range, list_trainers: list, has_legendary: bool= False, legendary_id: int = None, legendary_level: int = None):
        super().__init__(name, list_wild_pok_id, wild_pok_lvl_range, list_trainers)
        self.has_legendary = has_legendary
        if self.has_legendary:
            self.pokémon_legendary = Pokémon(pok_id= legendary_id, is_wild= True, level= legendary_level)
   
    def roaming(self, player: Player):
        counter = 1
        while True:
            print(self.name)
            if self.has_legendary and counter >= 10:
                print(f"What do you want to do ?:\n"
                      f"\t1| Find Trainer\n"
                      f"\t2| Roam through {self.name}\n"
                      f"\t3| You have found a stange pokémon!"
                )
            else:
                print(f"What do you want to do ?:\n"
                      f"\t1| Find Trainer\n"
                      f"\t2| Roam through {self.name}\n"
                )
            print(f"\tM| Open Menu"
                  f"\tE| Exit {self.name}")
            
            choice =input()
        
            if choice == 'e' or choice == 'E':
                break
            elif choice == 'm' or choice == 'M':
                menu(player= player)
                continue
            try:
                choice_int = int(choice)
            except ValueError:
                choice_int = 0
            match choice_int:
                case 0:
                    print("Invalid input!")
                    sleep(1)
                case 1:
                    clearscreen()
                    if self.trainers == None:
                        print("There is no traniers in this road!")
                        sleep(1)
                        clearscreen()
                    else:
                        trainers_index = 0
                        if trainers_index >= 0 and trainers_index < len(self.trainers):
                            battle(player= player, opponent= self.trainers[trainers_index])
                            if self.trainers[trainers_index].has_lost_vs_player:
                                trainers_index += 1
                        else:
                            if not self.has_beaten_all_trainer:
                                self.has_beaten_all_trainer = True
                            else:
                                print("You have already beaten all the trainers on this road!")
                                sleep(1)
                                clearscreen()
                case 2:
                    if self.wild_pok_id_available == None:
                        continue
                    else:
                        sleep(1)
                        clearscreen()
                        pok_index = random.randint(0, len(self.wild_pok_id_available) - 1)
                        pok_level = random.randint(0, len(self.wild_pok_level_range) - 1)
                        if random.randint(0,100) <= 50:
                            battle(
                                player= player, 
                                opponent= Pokémon(
                                    pok_id= self.wild_pok_id_available[pok_index],
                                    is_wild= True, 
                                    level= self.wild_pok_level_range[pok_level]
                                )
                            )
                case 3:
                    if self.has_legendary and counter >= 10:
                        clearscreen()
                        print(f"You have discovered the legendary pokémon {self.pokémon_legendary.name}")
                        sleep(1)
                        battle(player= player, opponent= self.pokémon_legendary)
                    else:
                        continue