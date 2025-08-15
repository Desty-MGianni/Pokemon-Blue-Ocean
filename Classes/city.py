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
                                pokémon.is_ko = False
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
            choice = input("Where do you want to go? \n" \
            "\t1| Pokémon Center \n" \
            "\t2| Pokémon Shop \n" \
            "\t3| Pokémon Gym\n" \
            "\tM| Menu\n"
            "\tE| Exit\n")
            if choice == 'e' or choice == 'E':
                break
            elif choice == 'm' or choice == 'M':
                menu(player= player)
                continue
            else:
                try:
                    choice_int = int(choice)
                except ValueError:
                    choice_int = 0
                
                match choice_int:
                    case 1:
                        self._pokemon_center(player= player)
                    case 2:
                        self.shop.shop(player= player)
                    case 3:
                        self.arena.arena_loop(player= player)
                    case _:
                        continue

class End(City):
    pokémon_master_defeated = False
    
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
                            End.pokémon_master_defeated = True
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
            "\tM| Menu\n" \
            "\tE| Exit\n")
            if player_choice == 'E' or player_choice == 'e':
                break
            elif player_choice == 'M' or player_choice == 'm':
                menu(player= player)
                continue
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
                        if player.inventory.has_all_badges:
                            if self.ligue_pokémon_loop(player= player):
                                # Trigger la fin du jeu
                                pass
                        else:
                            print("You can't enter the Pokémon tower as you don't have collected all the badges.")
                            sleep(1)
                            clearscreen()
                    case _:
                        continue

class Bourg_palette(City):
    def __init__(self):
        self.has_select_pokémon = False
        self.name = 'Bourg Palette'

    def roaming(self, player: Player):
        while True:
            print(self.name)
            choice = input("Where do you want to go ? \n"\
                    "\t1| Maison\n" \
                    "\t2| Labo du Professeur Chen\n"\
                    "\tM| Menu\n"
                    "\tE| Exit Bourg Palette\n" \
            )
            if choice == 'M' or choice == 'm':
                menu(player= player)
                continue

            elif choice == 'E' or choice == 'e':
                if self.has_select_pokémon:
                    break
                else:
                    print("You can't go through the routes without a Pokémon, it's too dangerous!")
                    sleep(2)
                    clearscreen()
            else:
                try:
                    choice_int = int(choice)
                except ValueError: 
                    choice_int = 0
                match choice_int:
                    case 0:
                        print("Please enter a number")
                    case 1:
                        self.home(player= player)
                    case 2:
                        self.prof_chen_visit(player= player)
                    case _:
                        continue
                
    def home(self, player: Player):
        print("Welcome Home!")
        for pokémon in player.list_pokémon:
            pokémon.is_ko = False
            pokémon.health = pokémon.max_health
        sleep(2)
        print("You and your pokémons have slept well")
        sleep(1)
        clearscreen()

    def prof_chen_visit(self, player: Player):
        if not self.has_select_pokémon:
            bulbizarre = Pokémon(pok_id= 1,level= 5)
            salamèche = Pokémon(pok_id= 4, level= 5)
            carapuce = Pokémon(pok_id= 7, level=5)
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
                clearscreen()
                print(f"Ok, {player.name}, now you need to choose your Pokémon starter!")
                print(f"\t1 | {bulbizarre.name}, {bulbizarre.type}\n" 
                    f"\t2 | {salamèche.name}, {salamèche.type}\n" 
                    f"\t3 | {carapuce.name}, {carapuce.type}\n"
                    )
                starter_choice = ''
                sleep(1)
                try:
                    starter_choice = int(input("Enter the corresponding number: "))
                except ValueError:
                    starter_choice = 0
                match starter_choice:
                    case 1:
                        print(f"You chose {bulbizarre.name}")
                        sleep(2)
                        player.list_pokémon.append(bulbizarre)
                        self.has_select_pokémon = True
                        del salamèche
                        del carapuce
                        break
                    case 2:
                        print(f"You chose {salamèche.name}")
                        sleep(2)
                        player.list_pokémon.append(salamèche)
                        self.has_select_pokémon = True
                        del bulbizarre
                        del carapuce
                        break
                    case 3:
                        print(f"You chose {carapuce.name}")
                        sleep(2)
                        player.list_pokémon.append(carapuce)
                        self.has_select_pokémon = True
                        del bulbizarre
                        del salamèche
                        break
                    case _:
                        continue
            print("Oh, I almost forgot, here is 5 Poké Ball to start your adventure! Gook luck!")
            player.inventory.update_inventory(item= "Poké Ball",quantity= 5)
            sleep(2)
            clearscreen()
        else:
            print("You have nothing to do at prof Chen's Lab!")
            sleep(1)
            clearscreen()
        