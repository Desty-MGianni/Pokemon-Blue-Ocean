from time import sleep
from Classes.menu import Menu
from Classes.battle import battle
from Classes.arena import Arena
from Classes.pokemon import Pokémon
from Classes.shop import Shop
from Classes.trainer import Player, Trainer
from Classes.clearscreen import clearscreen



class City(Menu):
    def __init__(self, name: str, has_arena: bool, shop_rank: str, arena_info: dict = None):
        self.name = name
        if has_arena:
            self.arena = Arena(arena_info['Name'],arena_info['Liste Dresseurs'],arena_info['Champion'],arena_info['Nom Badge'])
        self.shop = Shop(rank_shop= shop_rank, city_name= self.name)
        
    def _pokemon_center(self, player: Player):
        while True:
            print(f"You are in {self.name}'s Pokémon center!")
            choice = input("What do you want to do ? "
                            "\n\t1| Go to the nurse." 
                            "\n\t2| Go to the PC. "
                            "\n\tE| Exit \n")
            if choice == 'e' or choice == 'E':
                print("Thank you for you visit!")
                sleep(1)
                clearscreen()
                break
            try:
                choice = int(choice)
            except ValueError:
                choice = -1
            match choice:
                case 1:
                    heal_input = input("Hello! Do you want me to heal your Pokémons ? Y/n\n").lower()
                    match heal_input:
                        case 'n' | 'no':
                            clearscreen()
                            continue
                        case _:
                            sleep(0.5)
                            print('.')
                            sleep(0.5)
                            print('.')
                            sleep(0.5)
                            print('.')
                            sleep(0.5)
                            for pokémon in player.list_pokémon:
                                pokémon.health = pokémon.max_health
                            print('Your Pokémons have been treated, they are in great shape!')
                            sleep(1)
                            clearscreen()
                case 2:
                    sleep(1)
                    clearscreen()
                    player.inventory.interact_with_pc(player= player)
                    clearscreen()
                case _:
                    print("Invalid input!")
                    sleep(0.5)
                    continue
    def roaming(self, player: Player):
        while True:
            print(self.name)
            player_choice = input("Where do you want to go? \n" \
            "\t1| Pokémon Center \n" \
            "\t2| Pokémon Shop \n" \
            "\t3| Pokémon Gym\n" \
            "Enter 1 - 2 - 3 or type exit\n")
            if player_choice == 'Exit' or player_choice == 'exit':
                break
            else:
                try:
                    player_choice = int(player_choice)
                except ValueError:
                    player_choice = 0
                
                match player_choice:
                    case 1:
                        self.__pokemon_center(player= player)
                    case 2:
                        self.shop.shop(player= player)
                    case 3:
                        self.arena.arena_loop(player= player)
                    case _:
                        continue

class End(City):
    def __init__(self):
        self.name = "Plateau Indigo"
        self.shop = Shop(rank_shop= 'Max',city_name= 'Plateau Indigo')
        self.council_1 = Trainer(name= "Agatha", list_pokémon= [Pokémon(pok_id= 34)])
        self.council_2 = Trainer(name= "Aldo", list_pokémon= [Pokémon(pok_id= 34)])
        self.council_3 = Trainer(name= "Olga", list_pokémon= [Pokémon(pok_id= 34)])
        self.council_4 = Trainer(name= "Pieter", list_pokémon= [Pokémon(pok_id= 34)])
        self.master = Trainer(name= "Regis", list_pokémon= [Pokémon(pok_id= 34)])
    
    def ligue_pokémon_loop(self,player: Player):
        battle(player= player, opponent= self.council_1)
        if self.council_1.has_lost_vs_player:
            battle(player= player, opponent= self.council_2)
            if self.council_2.has_lost_vs_player:
                battle(player= player, opponent= self.council_3)
                if self.council_3.has_lost_vs_player:
                    battle(player= player, opponent= self.council_4)
                    if self.council_4.has_lost_vs_player:
                        battle(player= player, opponent= self.master)
                        if self.master.has_lost_vs_player:
                            return True
        self.council_1.has_lost_vs_player = False
        self.council_2.has_lost_vs_player = False
        self.council_3.has_lost_vs_player = False
        self.council_4.has_lost_vs_player = False
        return False
    def roaming(self, player):
        while True:
            print(self.name)
            player_choice = input("Where do you want to go? \n" \
            "\t1| Pokémon Center \n" \
            "\t2| Pokémon Shop \n" \
            "\t3| League Tower\n" \
            "Enter 1 - 2 - 3 or type exit\n")
            if player_choice == 'Exit' or player_choice == 'exit':
                break
            else:
                try:
                    player_choice = int(player_choice)
                except ValueError:
                    player_choice = 0
                match player_choice:
                    case 1:
                        super()._pokemon_center(player= player)
                    case 2:
                        self.shop.shop(player= player)
                    case 3:
                        if self.ligue_pokémon_loop(player= player):
                            # Trigger la fin du jeu
                            pass
                    case _:
                        continue

class Bourg_palette(City):
    def __init__(self):
        self.name = 'Bourg Palette'
    def roaming(self):
        choice = input("Where do you want to go ? \n"\
                       "\t1| Route 1\n")
        