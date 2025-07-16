from math import floor
from Classes.pokemon import Pokémon

class Inventory:
    # constructor with nothing in it as there will not be another instance of inventory except player's Inventory.
    def __init__(self):
        self.balls = {'Poké Ball': 0, 'Super Ball': 0, 'Hyper Ball': 0, 'Master Ball': 0}
        self.potions = {'Potion': 0, 'Super Potion': 0, 'Hyper Potion': 0, 'Potion Max': 0}
        self.stones = {'Pierre Feu': 0,'Pierre Eau': 0, 'Pierre Feuille': 0,'Pierre Foudre': 0, 'Pierre Lune': 0}
        self.revives = {'Rappel': 0, 'Rappel Max': 0}
        self.badges = {'Boulder Badge': 0, 'Cascade Badge': 0, 'Thunder Badge': 0, 'Rainbow Badge': 0, 'Soul Badge': 0,'Marsh Badge': 0, 'Volcano Badge': 0, 'Earth Badge': 0}
        self.list_pokemon_pc = []
        self.money = 3000
        pass

    # ToString method. This logic filter every item we have to print.
    def __repr__(self):
        # nested function that filter every key that has a value > 0.
        def dict_0_filter(input_dict: dict):
            temp = {}
            for key, value in input_dict.items():
                 if value > 0:
                    temp.update({key: value})
            return temp
        
        # Calls of filter function for every dict.
        balls_available = dict_0_filter(self.balls)
        potions_available = dict_0_filter(self.potions)
        stones_available = dict_0_filter(self.stones)
        revives_available = dict_0_filter(self.revives)
        
        return "Inventory: \n" \
            f"\tMoney: {self.money} Poké-Dollars \n" \
            f"\tPoké balls: {balls_available} \n" \
            f"\tPotions: {potions_available} \n" \
            f"\tRappels: {revives_available} \n" \
            f"\tEvolution Stones: {stones_available}"
        
    # nested function that do the operations and return a bool for the return loop.
    def verify_name_in_inventory(item:str,quantity: int, dict_looked: dict):
        if item in dict_looked:
            dict_looked[item] += quantity
            return True
        return False
    
    def verify_quantity_in_dict(self, object_name: str, dict_looked: dict):
        if dict_looked[object_name] >= 0:
            return True
        else:
            return False
    
    # method that update the money after a win or a loss in a battle. Insure an upper and lower limit to the money the player possess. The amount is handled in battle method!.
    def manage_money(self, amount):
        Inventory.money += amount
        if Inventory.money <= 0:
            Inventory.money = 0
        elif Inventory.money >= 9999999:
            Inventory.money = 9999999

    def add_badge_and_no_duplicate(self, badge_name: str):
        if badge_name in Inventory.badges:
            if Inventory.badges[badge_name] == 0:
                Inventory.badges[badge_name] += 1
        else:
            print("Error on the name of the badge! It doesn't correspond to the badge dict.")

    def add_pok_pc(self,pokemon: Pokémon):
        Inventory.list_pokemon_pc.append(pokemon) 
    
    # method that add items (value) in the dict. we have a bool return loop so that we don't need to go through every dict.
    def add_inventory(self,item: str, quantity: int):
    
        # Calls of the verify_in_inventory functrion and implementation of the return loop.
        verify_result = self.verify_name_in_inventory(item,quantity,Inventory.balls)
        if not verify_result:
            verify_result = self.verify_name_in_inventory(item,quantity,Inventory.potions)
            if not verify_result:
                verify_result = self.verify_name_in_inventory(item,quantity,Inventory.revives)
                if not verify_result:
                    verify_result = self.verify_name_in_inventory(item,quantity,Inventory.stones)
                    if not verify_result:
                        print("Error: The item isn't in the database")
    
    # Nested method that will handle stone evolution. Cannot presice PLayer datatype because of circular import.
    def __use_stone(self,object_name: str,player):
        for pokémon in player.list_pokémon:
            if pokémon.check_stone_evolution(object_name):
                Inventory.stones[object_name] -= 1
                if not self.verify_quantity_in_dict(object_name= object_name, dict_looked= Inventory.stones):
                    break
    
    # Nested method thatill handle healing pokémon and set value to each potion's health regen
    def __use_potion(object_name: str, pokémon: Pokémon):
        if pokémon.health == pokémon.max_health:
            print("The pokémon selected is full life!")
            return False
        else:
            match object_name:
                case 'Potion':
                    pokémon.gain_health(30)
                    Inventory.potions[object_name] -=1
                case "Super Potion":
                    pokémon.gain_health(50)
                    Inventory.potions[object_name] -=1
                case "Hyper Potion":
                    pokémon.gain_health(120)
                    Inventory.potions[object_name] -=1
                case "Potion Max":
                    pokémon.gain_health(900)
                    Inventory.potions[object_name] -=1
            return True
        
    def __use_revive(object_name: str, pokémon: Pokémon):
        if pokémon.is_ko:
            pokémon.is_ko = False
            match object_name:
                case 'Rappel':
                    pokémon.health = 10
                    Inventory.revives[object_name] -=1
                case 'Rappel Max':
                    pokémon.health = floor(pokémon.max_health * 0.5)
                    Inventory.revives[object_name] -=1
            return True
        else:
            print("Can't use a revive on a pokémon that isn't KO!")
            return False

    def __use_ball(object_name: str, wild_pokémon: Pokémon, player):
        capture_chance = 0
        match object_name:
            case "Poké Ball":
                capture_chance = 15
                Inventory.balls[object_name] -= 1
            case "Super Ball":
                capture_chance = 25
                Inventory.balls[object_name] -= 1
            case "Hyper Ball":
                capture_chance = 50
                Inventory.balls[object_name] -= 1
            case "Master Ball":
                capture_chance = 100
                Inventory.balls[object_name] -= 1
        player.capture_pokemon(wild_pokémon, capture_chance)

    def use_item(self):
        