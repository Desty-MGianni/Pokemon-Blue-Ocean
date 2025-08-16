import json
import beaupy
from time import sleep
from Classes.trainer import Player, Trainer
from Classes.clearscreen import clearscreen


def menu(player: Player):

    def save_serialization():
        var_to_dump = {
            "Player": {
                "name": player.name,
                "list pokémon": [
                    player
                ],
                "inventory": {
                    "money": player.inventory.money,
                    "balls": player.inventory.balls,
                    "potions": player.inventory.potions,
                    "stones": player.inventory.stones,
                    "badges": player.inventory.badges,
                },
            "Trainers": Trainer.list_trainer_obj
            }

        }
        to_save = json.dumps(var_to_dump)
        print(to_save)
        sleep(10)

    def swap_pokémon():
        if len(player.list_pokémon) > 1:
            while True:
                print("\tSwap Pokémons")
                counter = 1
                choice_manip_1 = beaupy.select(player.list_pokémon, return_index= True, cursor= "--->")
                print(f"You have selected {player.list_pokémon[choice_manip_1].name}")
                choice_manip_2 = beaupy.select(player.list_pokémon, return_index= True)
                if choice_manip_1 == choice_manip_2:
                    continue
                else:
                    temp = player.list_pokémon[choice_manip_1]
                    player.list_pokémon[choice_manip_1] = player.list_pokémon[choice_manip_2]
                    player.list_pokémon[choice_manip_2] = temp
        else:
           input(player.list_pokémon[0])

    while True:
            clearscreen()
            list_options = [
                f"Swap Pokémons",
                f"Inventory",
                f"{player.name}",
                f"Save Game",
                f"Exit Menu",
                f"Quit Game"
            ]
            print("\tMenu:")
            choice = beaupy.select(options= list_options, return_index= True, cursor= "--->")
            match choice:
                case 0:
                    # Swap pokémons
                    swap_pokémon()
                case 1:
                    # Use items in inventory
                    while True:
                        if not player.use_item(in_battle_vs_trainer= False, in_battle_vs_wild_pok= False):
                            break
                case 2:
                    # Show player, pok and inventory
                    input(player)
                case 3:
                    # Save game
                    save_serialization()
                case 4:
                    # Quit menu
                    sleep(1)
                    clearscreen()
                    break
                case 5:
                    # Quit game
                    if beaupy.confirm("Are you sure you want to quit the game?"):
                        clearscreen()
                        print("Thank you for playing my game!")
                        sleep(3)
                        clearscreen()
                        exit()
                case _:
                    pass

                        
