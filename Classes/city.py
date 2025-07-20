from time import sleep
from Classes.arena import Arena
from Classes.shop import Shop
from Classes.trainer import Player

class City:
    def __init__(self, name: str, has_arena: bool, shop_rank: str, arena_info: dict = None):
        self.name = name
        if has_arena:
            self.arena = Arena(arena_info['Name'],arena_info['Liste Dresseurs'],arena_info['Champion'],arena_info['Nom Badge'])
        self.shop = Shop(rank_shop= shop_rank, city_name= self.name)
        
    def __pokemon_center(self, player: Player):
        while True:
            print(f"You are in {self.name}'s Pokémon center!")
            try:
                choice = int(input("What do you want to do ? \n1| Go to the nurse. \n2| Go to the PC. \n3| Exit"))
            except ValueError:
                choice = -1
            match choice:
                case 1:
                    heal_input = input("Hello! Do you want me to heal your Pokémons ? Y/n").lower()
                    match heal_input:
                        case 'n' | 'no':
                            break
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
                case 2:
                    for pokémon in player.inventory.list_pokemon_pc:
                        print(pokémon)
                case 3:
                    print("Thank you for you visit!")
                    sleep(1)
                    break
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
            "\t3| Pokémon Gym\n")
            ""