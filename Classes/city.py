import beaupy
from time import sleep
from Classes.menu import menu
from Classes.battle import battle
from Classes.arena import Arena
from Classes.pokemon import Pokémon
from Classes.shop import Shop
from Classes.trainer import Player, Trainer
from Classes.clearscreen import clearscreen


# All the instances of ths classes are created in gen_map.py
class City():

    def __init__(self, name: str, has_arena: bool, shop_rank: str, arena_info: dict = None) -> None:
        self.name: str = name
        if has_arena:
            self.arena: Arena = Arena(
                arena_info['Name'],
                arena_info['Liste Dresseurs'],
                arena_info['Champion'],
                arena_info['Nom Badge']
            )
        self.shop: Shop = Shop(rank_shop= shop_rank, city_name= self.name)
    
    # The PC interactions in the game are handled with a method in Inventory class but is caled in __pokemoin_center method
    def _pokemon_center(self, player: Player) -> None:
        while True:
            print(f"\tYou are in {self.name}'s Pokémon center!")
            options: list[str] = [
                "Go to the nurse.",
                "Go to the PC.",
                "Exit"
            ]
            choice: int = beaupy.select(
                options= options, 
                return_index= True,
                cursor= "--->"
            )
            match choice:
                case 0:
                    if not beaupy.confirm(question= "Hello and welcome! Do you want me to heal your Pokémons?", cursor= "--->"):
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
                    clearscreen()
                    break
                case _:
                    print("Invalid input!")
                    sleep(0.5)
                    
    # called in main.game_loop, Act as a hub for all the Classes that directly inherit this method or that simply have the same name. (For Raod and Site classes).
    def roaming(self, player: Player) -> None:
        while True:
            options: list[str] = [
                f"Pokémon Center",
                f"Pokémon Shop",
                f"Pokémon Gym\n",
                f"Open Menu",
                f"Exit {self.name}"
            ]
            print(f"\t{self.name}")
            choice: int = beaupy.select(
                options= options, 
                return_index= True, 
                cursor= "--->"
            )
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

# Inherit principaly to have shop and pokémon_center methods and atributes. Has the end game loop built in.
# Has only 1 instances, created in gen_map.py
class End(City):
    # used to trigger the end of the game
    pokémon_master_defeated: bool = False 
    
    def __init__(self) -> None:
        self.name: str = "Plateau Indigo"
        self.shop: Shop = Shop(rank_shop= 'Max',city_name= 'Plateau Indigo')
        self.council_4: list[Trainer] = [
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
        self.master: Trainer = Trainer(
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
    
    # End game long run, like in the original games, all. the member are reset and we have to chain oll 5 fights
    def ligue_pokémon_loop(self,player: Player) -> bool:
        
        # after all the fights with council 4 member, this methed is called so that player can heal/revive it's pokémons
        def __pause_menu() -> None:
            if beaupy.confirm("Do you want to take a break and open menu?"):
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
        # when we lose vs a memeber of the council 4, we reset has_lost_vs_player attribute and heal all the pokémons.
        for member in self.council_4:
            member.has_lost_vs_player = False
            for pokemon in member.list_pokémon:
                pokemon.health = pokemon.max_health
        return False
    
    # Override of roaming method so that correspond to the end of the game
    def roaming(self, player: Player) -> None:
        if End.pokémon_master_defeated == False:
            while True:
                print(f"\t{self.name}")
                options: list[str] = [
                    f"Pokémon Center",
                    f"Pokémon Shop",
                    f"League Tower\n",
                    f"Open Menu",
                    f"Exit {self.name}"
                ]
                choice: int = beaupy.select(
                    options= options, 
                    return_index= True, 
                    cursor= "--->"
                )
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

# Hometown of player (starting spot for the game)
# Has only 1 instances, created in gen_map.py
class Bourg_palette(City):
    
    def __init__(self) -> None:
        self.has_select_pokémon: bool = False
        self.name: str = 'Bourg Palette'

    def roaming(self, player: Player) -> None:
        while True:
            clearscreen()
            print(f"\t{self.name}")
            options: list[str] = [
                f"Home",
                f"Professeur Chen's Lab\n",
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
    
    # Hometown version of the pokémon center          
    def home(self, player: Player) -> None:
        clearscreen()
        print("Welcome Home!")
        for pokémon in player.list_pokémon:
            pokémon.is_ko = False
            pokémon.health = pokémon.max_health
        sleep(2)
        print("You and your pokémons have slept well")
        sleep(1)
        clearscreen()
    
    # Used to get the pokémon starter
    def prof_chen_visit(self, player: Player) -> None:
        clearscreen()
        if not self.has_select_pokémon:
            starters: list[Pokémon] = [
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
                options = [
                    f"{starters[0].name}, {starters[0].type}",
                    f"{starters[1].name}, {starters[1].type}",
                    f"{starters[2].name}, {starters[2].type}"
                ]
                choice: int = beaupy.select(
                    options, 
                    return_index= True, 
                    cursor= "--->"
                )
                if choice == None:
                    continue
                if beaupy.confirm(question= f"Are you sure you want to select {starters[choice].name}?", cursor= "--->"):
                    print(f"You choose {starters[choice].name}")
                    sleep(2)
                    player.list_pokémon.append(starters[choice])
                    self.has_select_pokémon = True
                    del starters
                    break
            print("Oh, I almost forgot, here is 5 Poké Ball to start your adventure! Gook luck!")
            player.inventory.update_inventory(item= "Poké Ball",quantity= 5)
            sleep(2)
            clearscreen()
        
        else:
            print("You have nothing to do at prof Chen's Lab!")
            sleep(1)
            clearscreen()
        