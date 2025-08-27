import beaupy
from time import sleep
from random import randint, choice
from Classes.battle import battle
from Classes.menu import menu
from Classes.trainer import Trainer, Player
from Classes.clearscreen import clearscreen
from Classes.pokemon import Pokémon


# All the inctances of Road are created in gen_map.py file
class Road:

    def create_wild_pokemon(self,id_available: list[int], level_available: range) -> Pokémon:
        return Pokémon(
            pok_id= choice(id_available),
            is_wild= True,
            level= choice(level_available)
        )
    
    def __init__(self, name: str,list_wild_pok_id: list[int], wild_pok_lvl_range: range, list_trainers: list[Trainer]):
        self.name: str = name
        self.trainers: list[Trainer] = list_trainers
        self.wild_pok_id_available: list[int] = list_wild_pok_id
        self.wild_pok_level_range: range = wild_pok_lvl_range
        self.has_beaten_all_trainer: bool = False

    # Like city based classes except here, on Road / Site classes, we can explore wild bushes to find wild pokémons.
    def roaming(self, player: Player) -> None:
        # Event that occurs when player has all the badges and is going to victory road
        if self.name == "Route 22" and player.inventory.has_all_badges():
            print("You have to prove that you can challenge the league!")
            sleep(2)
            battle(
                player, 
                opponent= Trainer(
                    name= "Rival Regis",
                    list_pokémon= [
                        Pokémon(pok_id= 18, level= 47),
                        Pokémon(pok_id= 65, level= 47),
                        Pokémon(pok_id= 111, level= 45),
                        Pokémon(pok_id= 59, level= 45),
                        Pokémon(pok_id= 130, level= 45),
                        Pokémon(pok_id= 3, level= 53)
                    ]
                )
            )
        while True:
            print(f"\t{self.name}")
            options: list[str] = [
                f"Find Trainer",
                f"Roam through the bushes\n",
                f"Open Menu",
                f"Exit {self.name}"
            ]
            choice: int = beaupy.select(
                options, 
                return_index= True, 
                cursor= "--->"
            )
            match choice:
                case 0:
                    clearscreen()
                    if self.trainers == None:
                        print("There is no traniers in this road!")
                        sleep(1)
                        clearscreen()
                    else:
                        trainers_index: int = 0
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
                case 1:
                    sleep(1)
                    clearscreen()
                    if randint(0,100) <= 50:
                        opponent: Pokémon = self.create_wild_pokemon(
                            id_available= self.wild_pok_id_available,
                            level_available= self.wild_pok_level_range   
                        )
                        battle(player, opponent)
                case 2:
                    menu(player= player)
                case 3:
                    break
                case _:
                    clearscreen()
                    pass

# The only difference of this class is the presense of a legendary pokémon or not, decided in the call (in gen_map.py)
class Site(Road):
    def __init__(
            self, name: str, 
            list_wild_pok_id: list[int], 
            wild_pok_lvl_range: range, 
            list_trainers: list[Trainer], 
            has_legendary: bool= False, 
            legendary_id: int = None, 
            legendary_level: int = None) -> None:
        
        super().__init__(name, list_wild_pok_id, wild_pok_lvl_range, list_trainers)
        self.has_legendary: bool = has_legendary
        if self.has_legendary:
            self.pokémon_legendary: Pokémon = Pokémon(pok_id= legendary_id, is_wild= True, level= legendary_level)
   
    def roaming(self, player: Player):
        legen_counter: int = 1
        while True:
            print(f"\t{self.name}")
            options: list[str] = [
                f"Find Trainer",
                f"Roam through {self.name}\n",
                f"Open Menu",
                f"Exit {self.name}",
            ]
            if self.has_legendary and legen_counter >= 15:
                options[1] = f"Roam through {self.name}"
                options.insert(
                    index= 2,
                    object= f"You have found a stange pokémon!"
                )
            choice: str = beaupy.select(
                options,
                return_index= False,
                cursor= "--->"
            )
            if choice == f"Find Trainer":
                clearscreen()
                if self.trainers == None:
                    print("There is no traniers in this road!")
                    sleep(1)
                    clearscreen()
                else:
                    trainers_index: int = 0
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
            elif choice == f"Roam through {self.name}" or choice == f"Roam through {self.name}\n":
                if self.wild_pok_id_available == None:
                    print(f"There is no Pokémon to be seen in {self.name}")
                    sleep(1)
                    continue
                else:
                    sleep(1)
                    clearscreen()
                    if randint(0,100) <= 50:
                        opponent: Pokémon = super().create_wild_pokemon(
                            id_available= self.wild_pok_id_available,
                            level_available= self.wild_pok_level_range)
                        battle(player,opponent)
                        legen_counter += 1
            elif choice == "You have found a strange Pokémon!":
                clearscreen()
                print(f"You have discovered the legendary pokémon {self.pokémon_legendary.name}")
                sleep(1)
                battle(player= player, opponent= self.pokémon_legendary)

            elif choice == "Open Menu":
                menu(player= player)
            elif choice == f"Exit {self.name}":
                break
            else:
                pass