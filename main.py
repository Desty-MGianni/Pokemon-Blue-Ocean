import beaupy
from time import sleep
from Classes import gen_map
from Classes.clearscreen import clearscreen
from Classes.trainer import Player
from Classes.city import End, City, Bourg_palette
from Classes.road import Road, Site


"""
Pokémon Blue Ocean, 3rd gen Green Leav and Red Flame fan made with python From Desty
All the names of the cities, roads, sites, trainers and pokémons are in french because it's my motherly language and I thought it was fum!
"""


def start_menu() -> None:
    clearscreen()
    title_str: str = """
    ██████╗  ██████╗ ██╗  ██╗███████╗███╗   ███╗ ██████╗ ███╗   ██╗                 
    ██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝████╗ ████║██╔═══██╗████╗  ██║                 
    ██████╔╝██║   ██║█████╔╝ █████╗  ██╔████╔██║██║   ██║██╔██╗ ██║                 
    ██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║                 
    ██║     ╚██████╔╝██║  ██╗███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║                 
    ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝                 
                                                                                    
    ██████╗ ██╗     ██╗   ██╗███████╗     ██████╗  ██████╗███████╗ █████╗ ███╗   ██╗
    ██╔══██╗██║     ██║   ██║██╔════╝    ██╔═══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
    ██████╔╝██║     ██║   ██║█████╗      ██║   ██║██║     █████╗  ███████║██╔██╗ ██║
    ██╔══██╗██║     ██║   ██║██╔══╝      ██║   ██║██║     ██╔══╝  ██╔══██║██║╚██╗██║
    ██████╔╝███████╗╚██████╔╝███████╗    ╚██████╔╝╚██████╗███████╗██║  ██║██║ ╚████║
    ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝     ╚═════╝  ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝"""
    
    print(title_str)
    print(format("Made by Desty", '^75'))
    sleep(5)
    options: list[int] = [
        "New Game",
        "Exit"
    ]
    choice: str = beaupy.select(
        options= options, 
        return_index= False, 
        cursor= "--->"
    )
    match choice:
        case "New Game":
            pass
        case "Exit":
            clearscreen()
            exit()
        case _:
            pass

# Create an instance of player with personalized name
def creation_player() -> Player:
    while True:
        name: str = None
        if name is None:
            name = beaupy.prompt("What is your name? (between 3 and 15 character)")
            if len(name) < 3 or len(name) > 15:
                continue
            else:
                if beaupy.confirm(question= "confirm?", cursor= "--->"):
                    break
                else:
                    continue
    sleep(1)
    return Player(name= name, list_pokémon= [])

# Called within game_loop method, logic that handle where to look for in gen_map.py
def where_to_go(position: str) -> Road | Site | City | End | Bourg_palette:
    print("Where do you want to go? ")
    while True:
        destination: str = beaupy.select(
            options= gen_map.relation_map_dict[position], 
            preprocessor= lambda x : x.name, 
            return_index= True, 
            cursor= "--->"
        )
        if destination == None:
            continue
        return gen_map.relation_map_dict[position][destination]

"""
Infinite loop that that we dont break. Use of exit() function in 
    - start_menu in main.py
    - ligue_pokemon_loop in End class
    - in the menu.py
to exit the loop (game)
"""
def game_loop(player: Player) -> None:
    where_i_am: Road | City | Site | Bourg_palette | End = gen_map.bourg_palette
    while True:
        clearscreen()
        where_i_am.roaming(player= player)
        if End.pokémon_master_defeated:
            end_of_the_game()
        where_i_am = where_to_go(position= where_i_am)

# Called in ligue_pokemon_loop in End class when pokemon master is defeated
def end_of_the_game() -> None:
    print("Congratulation, You have finished the Game!")
    sleep(10)
    print("Thank you!")
    sleep(5)
    exit()

# Entry Point of the game
start_menu()
player = creation_player()
game_loop(player= player)