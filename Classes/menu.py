import beaupy
from time import sleep
from Classes.pokemon import Pokémon
from Classes.trainer import Player
from Classes.clearscreen import clearscreen

def menu(player: Player):

    def swap_pokémon() -> None:
        if len(player.list_pokémon) == 0:
            print("Go to the lab to receive your first pokémon!")
            sleep(1)
        elif len(player.list_pokémon) > 1:
            while True:
                print("\tSwap Pokémons")
                counter: int = 1
                choice_manip_1: int = beaupy.select(
                    options= player.list_pokémon, 
                    return_index= True, 
                    cursor= "--->"
                )
                if choice_manip_1 is not None:
                    print(f"You have selected {player.list_pokémon[choice_manip_1].name}")
                    choice_manip_2: int = beaupy.select(
                        player.list_pokémon, 
                        return_index= True, 
                        cursor= "--->"
                    )
                    if choice_manip_2 is not None:
                        if choice_manip_1 == choice_manip_2:
                            continue
                        else:
                            temp: Pokémon = player.list_pokémon[choice_manip_1]
                            player.list_pokémon[choice_manip_1] = player.list_pokémon[choice_manip_2]
                            player.list_pokémon[choice_manip_2] = temp
                break
        else:
           input(player.list_pokémon[0])
    
    # Entry point of menu function
    while True:
            clearscreen()
            options: list[str] = [
                f"Swap Pokémons",
                f"Use Item",
                f"{player.name}\n",
                f"Exit Menu",
                f"Quit Game"
            ]
            print("\tMenu:")
            choice: int = beaupy.select(
                options= options, 
                return_index= True, 
                cursor= "--->")
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
                    # Exit menu
                    clearscreen()
                    break
                case 4:
                    # Quit game
                    if beaupy.confirm(question= "Are you sure you want to quit the game?", cursor= "--->"):
                        clearscreen()
                        print("Thank you for playing my game!")
                        sleep(3)
                        clearscreen()
                        exit()
                case _:
                    pass

                        

