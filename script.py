import os
import beaupy
from time import sleep
from Classes import gen_map
from Classes.clearscreen import clearscreen
from Classes.trainer import Player

"""
Pokémon Blue Ocean, 3rd gen Green Leav and Red Flame fan made with python From Desty
All the names of the cities, roads, sites, trainers and pokémons are in french because it's my motherly language and I thought it was fum!

"""
def start_menu():
    list_option = [
        "New Game",
        "Exit"
    ]
    has_save = os.path.isfile("saves/save.json")
    if has_save:
        list_option.insert(0, "Continue")
    choice = beaupy.select(
        options= list_option, 
        return_index= False, 
        cursor= "--->"
    )
    match choice:
        case "New Game":
            pass
        case "Continue":
            # Deserialize
            pass
        case "Exit":
            clearscreen()
            exit()
        case _:
            pass


def creation_player():
    '''Create an instance of player with personalized name'''
    name = input("What is your name?\n")
    sleep(1)
    return Player(name= name, list_pokémon= [])

def where_to_go(position: str):
    ''' Called within game_loop method, logic that handle where to look for in gen_map.py'''
    print("Where do you want to go? ")
    destination = beaupy.select(
        options= gen_map.relation_map_dict[position], 
        preprocessor= lambda x : x.name, 
        return_index= True, 
        cursor= "--->"
    )
    return gen_map.relation_map_dict[position][destination]

def game_loop(player: Player):
    where_i_am = gen_map.bourg_palette
    while True:
        clearscreen()
        where_i_am.roaming(player= player)
        where_i_am = where_to_go(position= where_i_am)

def end_of_the_game():
    print("Congratulation, You have finished the Game!")
    sleep(10)
    print("Credits: This game has been made at 99,9% by me, Desty!")
    sleep(5)
    print("Thank you!")
    sleep(5)
    exit()

'''
Entry Point of the game
'''
clearscreen()
title_string= """                                         
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
╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝     ╚═════╝  ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                                                                                                                                                                                                                                                                                                                                                                                               
""".strip()
print(title_string)
print(format("Made by Desty", '^75'))
sleep(5)

start_menu()
player = creation_player()
game_loop(player= player)