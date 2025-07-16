from Classes.pokemon import Pokémon
from math import floor

class Inventory:
    balls = {'Poké Ball': 0, 'Super Ball': 0, 'Hyper Ball': 0, 'Master Ball': 0}
    potions = {'Potion': 0, 'Super Potion': 0, 'Hyper Potion': 0, 'Potion Max': 0}
    stones = {'Pierre Feu': 0,'Pierre Eau': 0, 'Pierre Feuille': 0,'Pierre Foudre': 0, 'Pierre Lune': 0}
    revives = {'Rappel': 0, 'Rappel Max': 0}
    badges = {'Boulder Badge': 0, 'Cascade Badge': 0, 'Thunder Badge': 0, 'Rainbow Badge': 0, 'Soul Badge': 0,'Marsh Badge': 0, 'Volcano Badge': 0, 'Earth Badge': 0}
    list_pokemon_pc = []
    money = 3000
    # constructor with nothing in it as there will not be another instance of inventory except player's Inventory.
    def __init__(self):
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
        balls_available = dict_0_filter(Inventory.balls)
        potions_available = dict_0_filter(Inventory.potions)
        stones_available = dict_0_filter(Inventory.stones)
        revives_available = dict_0_filter(Inventory.revives)
        
        return "Inventory: \n" \
            f"\tMoney: {Inventory.money} Poké-Dollars \n" \
            f"\tPoké balls: {balls_available} \n" \
            f"\tPotions: {potions_available} \n" \
            f"\tRappels: {revives_available} \n" \
            f"\tEvolution Stones: {stones_available}"
        
    # method that add items (value) in the dict. we have a bool return loop so that we don't need to go through every dict.
    def add_inventory(self,item: str, quantity: int):
        # nested function that do the operations and return a bool for the return loop.
        def verify_in_inventory(item:str,quantity: int, input_dict: dict):
            if item in input_dict:
                input_dict[item] += quantity
                return True
            return False
    
        # Calls of the verify_in_inventory functrion and implementation of the return loop.
        verify_result = verify_in_inventory(item,quantity,Inventory.balls)
        if not verify_result:
            verify_result = verify_in_inventory(item,quantity,Inventory.potions)
            if not verify_result:
                verify_result = verify_in_inventory(item,quantity,Inventory.revives)
                if not verify_result:
                    verify_result = verify_in_inventory(item,quantity,Inventory.stones)
                    if not verify_result:
                        print("Error: The item isn't in the database")