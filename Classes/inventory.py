import random
import beaupy
from time import sleep
from math import floor
from Classes.clearscreen import clearscreen
from Classes.pokemon import Pokémon

class Inventory:
    
    def __init__(self) -> None:
        self.balls: dict[str: int] = {'Poké Ball': 0, 'Super Ball': 0, 'Hyper Ball': 0, 'Master Ball': 0}
        self.potions: dict[str: int] = {'Potion': 0, 'Super Potion': 0, 'Hyper Potion': 0, 'Potion Max': 0}
        self.stones: dict[str: int] = {'Pierre Feu': 0,'Pierre Eau': 0, 'Pierre Feuille': 0,'Pierre Foudre': 0, 'Pierre Lune': 0}
        self.revives: dict[str: int] = {'Rappel': 0, 'Rappel Max': 0}
        self.badges: dict[str: int] = {'Boulder Badge': 0, 'Cascade Badge': 0, 'Thunder Badge': 0, 'Rainbow Badge': 0, 'Soul Badge': 0,'Marsh Badge': 0, 'Volcano Badge': 0, 'Earth Badge': 0}
        self.list_pokémon_pc: dict[str: int] = {"Boite 1": [], "Boite 2": [], "Boite 3": [], "Boite 4": [], "Boite 5": [], "Boite 6": [], "Boite 7": [], "Boite 8": [], "Boite 9": [], "Boite 10": []}
        self.money: int = 3000
        self.balls_available: dict[str: int] = {}
        self.potions_available: dict[str: int] = {}
        self.revives_available: dict[str: int] = {}
        self.stones_available: dict[str: int] = {}
    # We only want to show what we have in the inventory, so we filter all the keys where we at least have 1 in values
    def __str__(self) -> str:
        self.update_items_available()
        return "Inventory: \n" \
            f"\tMoney: {self.money} Poké-Dollars \n" \
            f"\tPoké balls: {self.balls_available} \n" \
            f"\tPotions: {self.potions_available} \n" \
            f"\tRappels: {self.revives_available} \n" \
            f"\tEvolution Stones: {self.stones_available}"

    def update_items_available(self):
        self.balls_available = Inventory.dict_0_filter(self.balls)
        self.potions_available = Inventory.dict_0_filter(self.potions)
        self.stones_available = Inventory.dict_0_filter(self.stones)
        self.revives_available = Inventory.dict_0_filter(self.revives)

    # Logic that return a dict without the keys -> volue = 0
    def dict_0_filter(input_dict: dict[str: int]) -> dict[str: int]:
        temp: dict[str: int] = {}
        for key, value in input_dict.items():
            if value > 0:
                temp.update({key: value})
        return temp
    
    def get_badges(self) -> dict[str: int]:
        return Inventory.dict_0_filter(input_dict= self.badges)

    def has_all_badges(self) -> bool:
        if self.badges.values() == [1,1,1,1,1,1,1,1]:
            return True
        else:
            return False
    
    def verify_name_in_dict(self, item: str, dict_looked: dict[str: int]) -> bool:
        if item in dict_looked:
            return True
        return False
    
    def verify_quantity_in_dict(self, object_name: str, dict_looked: dict[str: int]) -> bool:
        if dict_looked[object_name] > 0:
            return True
        else:
            return False
    
    def manage_money(self, amount: int) -> None:
        self.money += amount
        if self.money <= 0:
            self.money = 0
        elif self.money >= 9999999:
            self.money = 9999999

    def add_badge_and_no_duplicate(self, badge_name: str) -> None:
        if badge_name in self.badges:
            if self.badges[badge_name] == 0:
                self.badges[badge_name] += 1
        else:
            print("Error on the name of the badge! It doesn't correspond to the badge dict.")

    def add_pok_pc(self,pokemon: Pokémon) -> None:
        box_number: int = 1
        for box, pokémon_list in self.list_pokémon_pc.items():
            if len(pokémon_list) < 30:
                pokémon_list.append(pokemon)
                print(f"{pokemon.name} has been transfered to {box}")
                break
            else:
                box_number += 1

    def interact_with_pc(self, player) -> None: 
        box_number: int = 1
        while True:
            clearscreen()
            options: list[str] = [
                "Trade",
                "Take",
                "Deposit",
                "Exit"
            ]
            choice = beaupy.select(
                options,
                return_index= True,
                cursor= "--->"
            )
            match choice:
                case 0:
                    from_bag: bool = False
                    from_pc: bool = False
                    previous_box: str = ""
                    from_bag_index: int = -5
                    from_pc_index: int = -5
                    temp: None | Pokémon = None
                    while True:
                        clearscreen()
                        print(F"\tBoite {box_number}") 
                        if type(temp) == Pokémon:
                            print(f"Choose the pokémon you want to swap with {temp.name}")
                        options: list = player.inventory.list_pokémon_pc[f"Boite {box_number}"] + ["Next Box","Bag", "Exit"]
                        user_choice: int = beaupy.select(
                            options,
                            return_index= True,
                            cursor= "--->"
                        )
                        if user_choice < len(options) - 3:
                            if type(temp) == Pokémon:
                                if from_pc:
                                    player.inventory.list_pokémon_pc[previous_box][from_pc_index] = player.inventory.list_pokémon_pc[f"Boite {box_number}"][user_choice]
                                    player.inventory.list_pokémon_pc[f"Boite {box_number}"][user_choice] = temp
                                    temp = None
                                    from_pc = False

                                if from_bag:
                                    player.list_pokémon[from_bag_index] = player.inventory.list_pokémon_pc[f"Boite {box_number}"][user_choice]
                                    player.inventory.list_pokémon_pc[f"Boite {box_number}"][user_choice] = temp
                                    temp = None
                                    from_pc - False
                            else:
                                from_pc = True
                                from_pc_index = user_choice
                                previous_box= f"Boite {box_number}"
                                temp: Pokémon = player.inventory.list_pokémon_pc[previous_box][user_choice]
                                print(f"Select the pokémon you want to trade {temp.name} with:")
                        
                        elif user_choice == len(options) - 3:
                            box_number += 1
                            if box_number > 10:
                                box_number = 1
                            sleep(0.25)
                            continue
                        
                        elif user_choice == len(options) - 2:
                            index_bag = beaupy.select(
                                options= player.list_pokémon,
                                return_index= True,
                                cursor= "--->"
                            )
                            if type(temp) == Pokémon:
                                if from_bag:
                                    player.list_pokémon[from_bag_index] = player.list_pokémon[index_bag]
                                    player.list_pokémon[index_bag] = temp
                                    from_bag = False
                                    temp = None
                                if from_pc:
                                    player.inventory.list_pokémon_pc[previous_box][from_pc_index] = player.list_pokémon[index_bag]
                                    player.list_pokémon[index_bag] = temp
                                    from_pc = False
                                    temp = None
                            else:
                                from_bag = True
                                from_bag_index = index_bag
                                temp: Pokémon = player.list_pokémon[index_bag]
                                print(f"Select the pokémon you want to trade {temp.name} with:")
                        elif user_choice == len(options) - 1:
                            del temp
                            break
                case 1:
                    if len(player.list_pokémon) > 5:
                        print("You have already 6 pokémon with you!")
                        sleep(1)
                        break
                    while True:
                        print(f"\tBoite {box_number}")
                        options: list = self.list_pokémon_pc[f"Boite {box_number}"] + ["Next box", "Exit"]
                        choice_take: int = beaupy.select(
                            options,
                            return_index= True,
                            cursor= "--->"
                        )
                        if choice_take == len(options) - 1:
                            break
                        elif choice_take == len(options) - 2:
                            box_number +=1
                            if box_number > 10:
                                box_number = 1
                            continue
                        player.list_pokémon.append(self.list_pokémon_pc[f"Boite {box_number}"][choice_take])
                        self.list_pokémon_pc[f"Boite {box_number}"].pop(choice_take)
                        if len(player.list_pokémon) > 5:
                            break
                case 2:
                    if len(player.list_pokémon) <= 1:
                        print("You need to have at least one Pokémon with you!")
                        sleep(1)
                    else:
                        while True:
                            print("Select which pokémon to deposit: ")
                            options = player.list_pokémon + ["exit"]
                            choice = beaupy.select(
                                options,
                                return_index= True,
                                cursor= "--->"
                            )
                            if choice == options[-1]:
                                break
                            self.add_pok_pc(pokemon= player.list_pokémon[choice])
                            player.list_pokémon.pop(choice)
                case 3:
                    break
    # As the keys are fixed, only values are updated
    def update_inventory(self,item: str, quantity: int) -> None:
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
    
    def use_stone(self,stone: str, pokémon: Pokémon) -> bool:
            if pokémon.check_stone_evolution(stone):
                if beaupy.confirm(
                    question= f"{pokémon.name} can be evolved with {stone}. Do you want to proceed ?", 
                    cursor= "--->"
                ):
                    self.stones[stone] -= 1
                    sleep(0.5)
                    print("\t.")
                    sleep(1)
                    print("\t.")
                    sleep(1)
                    print("\t.")
                    print(f"Congratulaton! {pokémon.name} has evolved from {Pokémon.pok_table[pokémon.pok_id][0]} to ", end='')
                    pokémon.pok_id = Pokémon.evolution_stone_table[stone][pokémon.pok_id]
                    pokémon.max_health += random.randint(40,50)
                    pokémon.name = pokémon.set_name()
                    print(f"{Pokémon.pok_table[pokémon.pok_id][0]}")
                    sleep(3)
                    return True
                return False
            return False
    
    def use_potion(self,object_name: str, pokémon: Pokémon) -> bool:
        if pokémon.health == pokémon.max_health:
            print("The pokémon selected is full life!")
            return False
        else:
            self.potions[object_name] -= 1
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
    
    def use_revive(self,object_name: str, pokémon: Pokémon) -> bool:
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
    
    # compare to the other use_..., balls are only changind the odds of capturing a wild pokémon, i.e int return type.
    def use_ball(self,object_name: str) -> int:
        capture_chance: int = 0
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
        