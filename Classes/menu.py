from time import sleep
from Classes.trainer import Player
from Classes.clearscreen import clearscreen

def menu(player: Player):
    def swap_pokémon():
        while True:
            counter = 1
            for pokémon in player.list_pokémon:
                print(f"{counter}| {pokémon}")
                counter +=1
            choice_manip_1 = input("Enter the number corresponging the pokémon you want to swap: (c for cancel): ")
            if choice_manip_1 == 'c' or choice_manip_1 == 'C':
                break
            else:
                try:
                    choice_manip_1 = int(choice_manip_1)
                except ValueError:
                    choice_manip_1 = 0
                if choice_manip_1 > 0 and choice_manip_1 < 7:
                    print(f"You have selected {player.list_pokémon[choice_manip_1 - 1].name}")
                    choice_manip_2 = input("Enter the number of the the other pokémon to swap: (c for cancel): ")
                    if choice_manip_2 == 'c' or choice_manip_2 == 'C':
                        break
                    else:
                        try:
                            choice_manip_2 = int(choice_manip_2)
                        except ValueError:
                            choice_manip_2 = 0
                        if choice_manip_2 > 0 and choice_manip_2 < 7:
                            print(f"You have selected {player.list_pokémon[choice_manip_2 - 1].name}")
                            if choice_manip_1 == choice_manip_2:
                                continue
                            else:
                                temp = player.list_pokémon[choice_manip_1 - 1]
                                player.list_pokémon[choice_manip_1 -1] = player.list_pokémon[choice_manip_2 -1]
                                player.list_pokémon[choice_manip_2 -1] = temp
                        else:
                            print(f"Error typing the second pokémon to exchange")
                else:
                    print("Error typing the first pokémon to exchange")

    while True:
            clearscreen()
            choice = input("Menu\n" \
            f"\t1| Pokémon\n"
            f"\t2| Inventory\n" \
            f"\t3| {player.name}\n" \
            f"\tE| Exit Menu\n" \
            f"\tQ| Quit Game\n")

            if choice == 'E' or choice == 'e':
                sleep(1)
                clearscreen()
                break
            elif choice == 'Q' or choice == 'q':
                exit()
            else:
                try:
                    choice_int = int(choice)
                except ValueError:
                    choice_int = 0
                match choice_int:
                    case 1:
                        swap_pokémon()
                    case 2:
                        while True:
                            if not player.use_item(in_battle_vs_trainer= False, in_battle_vs_wild_pok= False):
                                break
                    case 3:
                        print(player)
                        sleep(5)
                    case 4:
                        pass
                        
