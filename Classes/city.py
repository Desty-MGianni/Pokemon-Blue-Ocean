import beaupy
from time import sleep
from Classes.menu import menu
from Classes.battle import battle
from Classes.arena import Arena
from Classes.pokemon import Pokémon
from Classes.shop import Shop
from Classes.trainer import Player, Trainer
from Classes.clearscreen import clearscreen



class City():

    def __init__(self, name: str, has_arena: bool, shop_rank: str, arena_info: dict = None):
        self.name = name
        if has_arena:
            self.arena = Arena(
                arena_info['Name'],
                arena_info['Liste Dresseurs'],
                arena_info['Champion'],
                arena_info['Nom Badge']
            )
        self.shop = Shop(rank_shop= shop_rank, city_name= self.name)
        
    def _pokemon_center(self, player: Player):
        while True:
            print(f"\tYou are in {self.name}'s Pokémon center!")
            list_options = [
                "Go to the nurse.",
                "Go to the PC.",
                "Exit"
            ]
            choice = beaupy.select(options= list_options, return_index= True, cursor= "--->")
            match choice:
                case 0:
                    heal = beaupy.confirm("Hello and welcome! Do you want me to heal your Pokémons?")
                    if not heal:
                        clearscreen()
                        continue
                    else:
                        sleep(0.5)
                        print('.')
                        sleep(0.5)
                        print('.')
                        sleep(0.5)
                        print('.')
                        sleep(0.5)
                        for pokémon in player.list_pokémon:
                            pokémon.is_ko = False
                            pokémon.health = pokémon.max_health
                        print('Your Pokémons have been treated, they are in great shape!')
                        sleep(1)
                        clearscreen()
                case 1:
                    sleep(1)
                    clearscreen()
                    player.inventory.interact_with_pc(player= player)
                    clearscreen()
                case 2:
                    break
                case _:
                    print("Invalid input!")
                    sleep(0.5)
                    
    
    def roaming(self, player: Player):
        while True:
            list_options = [
                f"Pokémon Center",
                f"Pokémon Shop",
                f"Pokémon Gym",
                f"Open Menu",
                f"Exit {self.name}"
            ]
            print(f"\t{self.name}")
            choice = beaupy.select(options= list_options, return_index= True, cursor= "--->")
            match choice:
                case 0:
                    self._pokemon_center(player= player)
                case 1:
                    self.shop.shop(player= player)
                case 2:
                    self.arena.arena_loop(player= player)
                case 3:
                    menu(player= player)
                case 4:
                    break
                case _:
                    pass
class End(City):
    
    def __init__(self):
        self.name = "Plateau Indigo"
        self.shop = Shop(rank_shop= 'Max',city_name= 'Plateau Indigo')
        self.council_4 = [
            Trainer(
                name= "Membre du Conseil 4 Olga", 
                list_pokémon= [
                    Pokémon(pok_id= 87, level= 52),
                    Pokémon(pok_id= 91, level= 51),
                    Pokémon(pok_id= 80, level= 52),
                    Pokémon(pok_id= 124, level= 54),
                    Pokémon(pok_id= 131, level= 54)
                ]
            ),       
            Trainer(
                name= "Membre du Conseil 4 Aldo", 
                list_pokémon= [
                    Pokémon(pok_id= 95, level= 51),
                    Pokémon(pok_id= 107, level= 53),
                    Pokémon(pok_id= 106, level= 53),
                    Pokémon(pok_id= 95, level= 54),
                    Pokémon(pok_id= 68, level= 56)
                ]
            ),
            Trainer(
                name= "Membre du Conseil 4 Agatha", 
                list_pokémon= [
                    Pokémon(pok_id= 94, level= 54),
                    Pokémon(pok_id= 42, level= 54),
                    Pokémon(pok_id= 93, level= 53),
                    Pokémon(pok_id= 24, level= 56),
                    Pokémon(pok_id= 94, level= 58)
                ]
            ),
            Trainer(
                name= "Membre du Conseil 4 Peter", 
                list_pokémon= [
                    Pokémon(pok_id= 130, level= 56),
                    Pokémon(pok_id= 147, level= 54),
                    Pokémon(pok_id= 147, level= 54),
                    Pokémon(pok_id= 142, level= 58),
                    Pokémon(pok_id= 149, level= 60)
                ]
            )
        ]
        self.master = Trainer(
            name= "Maitre Regis", 
            list_pokémon= [
                Pokémon(pok_id= 18, level= 59),
                Pokémon(pok_id= 65, level= 57),
                Pokémon(pok_id= 112, level= 59),
                Pokémon(pok_id= 59, level= 59),
                Pokémon(pok_id= 103, level= 61),
                Pokémon(pok_id= 9, level= 63)
            ]
        )
    
    def ligue_pokémon_loop(self,player: Player):
        def __pause_menu():
            pause_taken = beaupy.confirm("Do you want to take a break and open menu?")
            if pause_taken:
                menu(player= player)
        
        battle(player= player, opponent= self.council_4[0])
        __pause_menu()
        if self.council_1.has_lost_vs_player:
            battle(player= player, opponent= self.council_4[1])
            if self.council_2.has_lost_vs_player:
                __pause_menu()
                battle(player= player, opponent= self.council_4[2])
                if self.council_3.has_lost_vs_player:
                    __pause_menu()
                    battle(player= player, opponent= self.council_4[3])
                    if self.council_4.has_lost_vs_player:
                        __pause_menu()
                        battle(player= player, opponent= self.master)
                        if self.master.has_lost_vs_player:
                            return True
        for member in self.council_4:
            member.has_lost_vs_player = False
        return False
    
    def roaming(self, player):
        while True:
            print(f"\t{self.name}")
            list_options = [
                f"Pokémon Center \n",
                f"Pokémon Shop \n",
                f"League Tower\n\n",
                f"Open Menu\t",
                f"Exit {self.name}\n"
            ]
            choice = beaupy.select(options= list_options, return_index= True, cursor= "--->")
            match choice:
                case 0:
                    super()._pokemon_center(player= player)
                case 1:
                    self.shop.shop(player= player)
                case 2:
                    if player.inventory.has_all_badges:
                        if self.ligue_pokémon_loop(player= player):
                            End.pokémon_master_defeated = True
                    else:
                        print("You can't enter the Pokémon tower as you don't have collected all the badges.")
                        sleep(1)
                        clearscreen()
                case 3:
                    menu(player= player)
                case 4:
                    break
                case _:
                    continue

class Bourg_palette(City):
    def __init__(self):
        self.has_select_pokémon = False
        self.name = 'Bourg Palette'

    def roaming(self, player: Player):
        while True:
            print(f"\t{self.name}")
            list_options = [
                f"Home",
                f"Professeur Chen's Lab",
                f"Open Menu",
                f"Exit {self.name}"
            ]
            choice = beaupy.select(options= list_options, return_index= True, cursor= "--->")
            match choice:
                case 0:
                    self.home(player= player)
                case 1:
                    self.prof_chen_visit(player= player)
                case 2:
                    menu(player= player)
                case 3:
                    if self.has_select_pokémon:
                        break
                    else:
                        print("You can't go through the routes without a Pokémon, it's too dangerous!")
                        sleep(2)
                        clearscreen()
                case _:
                    continue
                
    def home(self, player: Player):
        clearscreen()
        print("Welcome Home!")
        for pokémon in player.list_pokémon:
            pokémon.is_ko = False
            pokémon.health = pokémon.max_health
        sleep(2)
        print("You and your pokémons have slept well")
        sleep(1)
        clearscreen()

    def prof_chen_visit(self, player: Player):
        clearscreen()
        if not self.has_select_pokémon:
            list_starters = [
                Pokémon(pok_id= 1,level= 5),
                Pokémon(pok_id= 4, level= 5),
                Pokémon(pok_id= 7, level=5)
            ]
            print(f"Hello {player.name} and welcome to my lab!")
            sleep(1)
            print(f"I suppose you are here to select you first Pokémon am I right ?")
            sleep(1)
            print(".")
            sleep(1)
            print(".")
            sleep(1)
            print(".")
            sleep(0.5)
            while True:
                print(f"Ok, {player.name}, now you need to choose your Pokémon starter!")
                print("Which pokémon will you select?")
                list_starters_options = [
                    f"{list_starters[0].name}, {list_starters[0].type}",
                    f"{list_starters[1].name}, {list_starters[1].type}",
                    f"{list_starters[2].name}, {list_starters[2].type}"
                ]
                choice = beaupy.select(list_starters_options, return_index= True, cursor= "--->")
                confirmation = beaupy.confirm(f"Are you sure you want to select {list_starters[choice].name}?")
                if confirmation:
                    print(f"You choose {list_starters[choice].name}")
                    sleep(2)
                    player.list_pokémon.append(list_starters[choice])
                    self.has_select_pokémon = True
                    del list_starters
                    break
            print("Oh, I almost forgot, here is 5 Poké Ball to start your adventure! Gook luck!")
            player.inventory.update_inventory(item= "Poké Ball",quantity= 5)
            sleep(2)
            clearscreen()
        
        else:
            print("You have nothing to do at prof Chen's Lab!")
            sleep(1)
            clearscreen()
        