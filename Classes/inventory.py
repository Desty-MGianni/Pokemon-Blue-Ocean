from time import sleep
from math import floor
from Classes.clearscreen import clearscreen
from Classes.pokemon import Pokémon

class Inventory:
    
    def __init__(self):
        self.balls = {'Poké Ball': 0, 'Super Ball': 0, 'Hyper Ball': 0, 'Master Ball': 0}
        self.potions = {'Potion': 0, 'Super Potion': 0, 'Hyper Potion': 0, 'Potion Max': 0}
        self.stones = {'Pierre Feu': 0,'Pierre Eau': 0, 'Pierre Feuille': 0,'Pierre Foudre': 0, 'Pierre Lune': 0}
        self.revives = {'Rappel': 0, 'Rappel Max': 0}
        self.badges = {'Boulder Badge': 0, 'Cascade Badge': 0, 'Thunder Badge': 0, 'Rainbow Badge': 0, 'Soul Badge': 0,'Marsh Badge': 0, 'Volcano Badge': 0, 'Earth Badge': 0}
        self.list_pokemon_pc = {"Boite 1": [], "Boite 2": [], "Boite 3": [], "Boite 4": [], "Boite 5": [], "Boite 6": [], "Boite 7": [], "Boite 8": [], "Boite 9": [], "Boite 10": []}
        self.money = 3000
        pass

    def __repr__(self):
    
        balls_available = Inventory.dict_0_filter(self.balls)
        potions_available = Inventory.dict_0_filter(self.potions)
        stones_available = Inventory.dict_0_filter(self.stones)
        revives_available = Inventory.dict_0_filter(self.revives)
        
        return "Inventory: \n" \
            f"\tMoney: {self.money} Poké-Dollars \n" \
            f"\tPoké balls: {balls_available} \n" \
            f"\tPotions: {potions_available} \n" \
            f"\tRappels: {revives_available} \n" \
            f"\tEvolution Stones: {stones_available}"

    def dict_0_filter(input_dict: dict):
        temp = {}
        for key, value in input_dict.items():
            if value > 0:
                temp.update({key: value})
        return temp
    
    def get_badges(self):
        return Inventory.dict_0_filter(input_dict= self.badges)

    def verify_name_in_dict(self, item: str, dict_looked: dict):
        if item in dict_looked:
            return True
        return False
    
    def verify_quantity_in_dict(self, object_name: str, dict_looked: dict):
        if dict_looked[object_name] > 0:
            return True
        else:
            return False
    
    def manage_money(self, amount):
        self.money += amount
        if self.money <= 0:
            self.money = 0
        elif self.money >= 9999999:
            self.money = 9999999

    def add_badge_and_no_duplicate(self, badge_name: str):
        if badge_name in self.badges:
            if self.badges[badge_name] == 0:
                self.badges[badge_name] += 1
        else:
            print("Error on the name of the badge! It doesn't correspond to the badge dict.")

    def add_pok_pc(self,pokemon: Pokémon):
        box_number = 1
        for box, pokémon_list in self.list_pokemon_pc.items():
            if len(pokémon_list) < 30:
                pokémon_list.append(pokemon)
                print(f"{pokemon.name} has been transfered to {box}")
                break
            else:
                box_number += 1

    def interact_with_pc(self,player):
        def Trade(box: str):
            print(len(player.list_pokémon))
            sleep(1)
            if len(player.list_pokémon) == 6:
                number = 1
                for pokémon in self.list_pokemon_pc[box]:
                    print(f"\t{number}| {pokémon}")
                    number += 1
                player_choice = input("Which pokémon do you want to take from PC ? Enter the corresponding number. Type exit to cancel\t").lower()
                if player_choice == "exit":
                    return False
                try:
                    player_choice= int(player_choice)
                except ValueError:
                    player_choice = 0
                if player_choice > 0 and player_choice <= 30:
                    pokémon_to_swap = self.list_pokemon_pc[box][player_choice - 1]
                    number_player_pok = 1
                    for pokémon in player.list_pokémon:
                        print(f"{number_player_pok} | {pokémon}")
                        number_player_pok += 1
                    try:
                        player_choice_list_pok = int(input("Type the number corresponding to te pokémon you want to swap. "))
                    except ValueError:
                        player_choice_list_pok = -1
                    if player_choice_list_pok > 0 and player_choice_list_pok <= 6:
                        self.list_pokemon_pc[box][player_choice - 1] = player.list_pokémon[player_choice_list_pok - 1]
                        player.list_pokémon[player_choice_list_pok - 1] = pokémon_to_swap
                        sleep(1)
                        clearscreen()
                        return True
                    else:
                        print("Input error! Try again")
                        return True
            
            elif len(player.list_pokémon) <= 5:
                number = 1
                for pokémon in self.list_pokemon_pc[box]:
                    print(f"\t{number}| {pokémon}")
                    number += 1
                player_choice = input("Which pokémon do you want to take from PC ? Enter the corresponding number. Type exit to cancel\n").lower()
                if player_choice == "exit":
                    return False
                try:
                    player_choice= int(player_choice)
                except ValueError:
                    player_choice = 0
                if player_choice > 0 and player_choice <= 30:
                    print(f"{self.list_pokemon_pc[box][player_choice - 1].name} has been added to your active pokémons!")
                    player.list_pokémon.append(self.list_pokemon_pc[box][player_choice - 1])
                    self.list_pokemon_pc[box].pop(player_choice - 1)
                    sleep(1)
                    return True
                return False
            
        box_number = 1
        while True:
            clearscreen()
            print(F"Boite {box_number}")
            for pok in self.list_pokemon_pc[f"Boite {box_number}"]:
                print(f"\t{pok}")
            print("Press enter to cycle through boxes. | Type trade to exchange with PC | Type deposit if you don't want to trade | Type exit to move on.")
            player_choice = input().lower()
            if player_choice == '':
                box_number += 1
                if box_number > 10:
                    box_number = 1
                sleep(0.25)
                clearscreen()
                continue
            elif player_choice == 'trade':
                if len(self.list_pokemon_pc[f"Boite {box_number}"]) == 0:
                    print("You can't trade when there is no pokémon in the box!")
                    sleep(1)
                    continue
                if not Trade(box= f"Boite {box_number}"):
                    break
            elif player_choice == 'deposit':
                if len(player.list_pokémon) == 1:
                    print("You have to have at least 1 pokémon! You can't deposit.")
                    sleep(1)
                else:
                    if len(self.list_pokemon_pc[f"Boite {box_number}"]) <= 30:
                        counter = 1
                        for pokémon in player.list_pokémon:
                            print(f"{counter} | {pokémon}")
                            counter += 1
                        try:
                            index_pokémon_to_deposit = int(input(f"Type the number corresponding to the pokémon you want to deposit in Boite {box_number}: "))
                        except ValueError:
                            index_pokémon_to_deposit = -1
                        if index_pokémon_to_deposit > 0 and index_pokémon_to_deposit < 7:
                            self.list_pokemon_pc[f"Boite {box_number}"].append(player.list_pokémon[index_pokémon_to_deposit - 1])
                            print(f"You have transfered {player.list_pokémon[index_pokémon_to_deposit - 1].name} to Boite {box_number}")
                            player.list_pokémon.pop(index_pokémon_to_deposit - 1)
                            sleep(1)
                            continue
            elif player_choice == 'exit':
                break
            else:
                clearscreen()
                ...

    def update_inventory(self,item: str, quantity: int):
    
        if self.verify_name_in_dict(item= item, dict_looked= self.balls):
            self.balls[item] += quantity
        elif self.verify_name_in_dict(item= item, dict_looked= self.potions):
            self.potions[item] += quantity
        elif self.verify_name_in_dict(item= item, dict_looked= self.revives):
            self.revives[item] += quantity
        elif self.verify_name_in_dict(item= item, dict_looked= self.stones):
            self.stones[item] += quantity
        else:
            print("Error: The item isn't in the database or there is a typo in object name!")
    
    def use_stone(self,object_name: str,pokémon: Pokémon):
        if pokémon.check_stone_evolution(object_name):
            self.stones[object_name] -= 1
            return True
        else:
            return False
    
    def use_potion(self,object_name: str, pokémon: Pokémon):
        if pokémon.health == pokémon.max_health:
            print("The pokémon selected is full life!")
            return False
        else:
            self.potion[object_name] -= 1
            match object_name:
                case 'Potion':
                    pokémon.gain_health(30)
                case "Super Potion":
                    pokémon.gain_health(50)
                case "Hyper Potion":
                    pokémon.gain_health(120)
                case "Potion Max":
                    pokémon.gain_health(900)
            return True
        
    def use_revive(self,object_name: str, pokémon: Pokémon):
        if pokémon.is_ko:
            pokémon.is_ko = False
            match object_name:
                case 'Rappel':
                    pokémon.health = 10
                    self.revives[object_name] -=1
                case 'Rappel Max':
                    pokémon.health = floor(pokémon.max_health * 0.5)
                    self.revives[object_name] -=1
            return True
        else:
            print("Can't use a revive on a pokémon that isn't KO!")
            return False

    def use_ball(self,object_name: str):
        capture_chance = 0
        match object_name:
            case "Poké Ball":
                capture_chance = 15
                self.balls[object_name] -= 1
            case "Super Ball":
                capture_chance = 25
                self.balls[object_name] -= 1
            case "Hyper Ball":
                capture_chance = 50
                self.balls[object_name] -= 1
            case "Master Ball":
                capture_chance = 100
                self.balls[object_name] -= 1
        return capture_chance
        