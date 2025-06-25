from Classes import (
    pokemon as pok)

class Inventory:
    balls = {'Poké Ball': 0, 'Super Ball': 0, 'Hyper Ball': 0, 'Master Ball': 0}
    potions = {'Potion': 0, 'Super Potion': 0, 'Hyper Potion': 0, 'Potion Max': 0}
    stones = {'Pierre Feu': 0,'Pierre Eau': 0, 'Pierre Feuille': 0,'Pierre Foudre': 0, 'Pierre Lune': 0}
    
    # constructor with nothing in it as there will not be another instance of inventory except player's Inventory.
    def __init__(self):
        pass

    # ToString method. This logic filter every item we have to print.
    def __repr__(self):
        # nested function that filter every key that has a value > 0.
        def dict_0_filter(input: dict):
            temp = {}
            for key, value in input.items():
                 if value > 0:
                    temp.update({key: value})
            return temp
        
        # Calls of filter function for every dict.
        balls_available = dict_0_filter(Inventory.balls)
        potions_available = dict_0_filter(Inventory.potions)
        stones_available = dict_0_filter(Inventory.stones)
        
        return f"Poké balls: {balls_available} \n" \
            f"Potions: {potions_available} \n" \
            f"Evolution Stones: {stones_available}"

    # method that add items (value) in the dict. we have a bool return loop so that we don't need to go through every dict.
    def add_inventory(self,item: str, quantity: int):
        # nested function that do the operations and return a bool for the return loop.
        def verify_in_inventory(item:str,quantity: int, input_dict: dict):
            if item in input_dict:
                input_dict[item] += quantity
                return True
            return False
        
        # Calls of the verifyP_in_inventory functrion and implementation of the return loop.
        verify_result = verify_in_inventory(item,quantity,Inventory.balls)
        if not verify_result:
            verify_result = verify_in_inventory(item,quantity,Inventory.potions)
            if not verify_result:
                verify_result = verify_in_inventory(item,quantity,Inventory.stones)
                if not verify_result:
                    print("Error: The item isn't in the database")
    
    # Method that will handle every dict and every item with nested method
    def use_item(self, in_battle:bool, battle_vs_pok: bool,player):
        
        # Nested method that will compare the input and every object dict.
        def dict_selector(input_str: str):
        
            # Nested method that check if you have an item and if true then we remove 1.
            def dict_action(input_str:str, collec: dict):
                if collec[input_str] > 0:
                    collec[input_str] -= 1
                    return True
                else:
                    return False
            
            # Nested method that will handle stone evolution.
            def evolution_with_stone(stone: str,player):
                for pokémon in player.list_pokémon:
                    print(pokémon)
                    print(pokémon.is_evolvable)
                    pokémon.check_stone_evolution(stone)

            # Nested method thatill handle healing pokémon and set value to each potion's health regen
            def use_potion(input_str: str, pokémon: pok.Pokémon):
                if pokémon.health == pokémon.max_health:
                    print("The pokémon selected is full life!")
                    return False
                else:
                    match input_str:
                        case 'Potion':
                            pokémon.gain_health(30)
                        case "Super Potion":
                            pokémon.gain_health(50)
                        case "Hyper Potion":
                            pokémon.gain_health(120)
                        case "Potion Max":
                            pokémon.gain_health(900)
                    return True
            
            def use_ball():
                pass
            
            # titalised the input to correspond the data in the Dicts.
            formatted_input = input_str.title()
            print(formatted_input)
            
            # Check if input is in balls dict and verify if 
            # 1. bool variable battle_vs_pok is True (as we can only capture pokémons if they're wild)
            # 2. the item is in the inventory by calling dict_action 
            if formatted_input in Inventory.balls:
                if battle_vs_pok:
                    if dict_action(formatted_input,Inventory.balls):
                        use_ball()
                else:
                    print("You can't capture a pokémon that's already been captured by another trainer.")
            
            # Check if input is in stones dict and verify if
            # 1. bool variable in_battle is False as we don't want to evolve pokémon with stones in a battle.
            # 2. the item is in the inventory by calling dict_action
            elif formatted_input in Inventory.stones:
                if not in_battle:
                    if dict_action(formatted_input, Inventory.stones):
                        evolution_with_stone(formatted_input, player)
                else: 
                    print("You can't use this item in a battle!")
            
            # Check if input is in potion dict and
            # 1 verify if the item is in the inventory
            # we loop so that the player can, if he failed, retry to set wich pokémon he want to heal.
            elif formatted_input in Inventory.potions: 
                if dict_action(formatted_input, Inventory.potions):
                    while True:
                        print(F"Which pokémon do you want to use {formatted_input}? (Enter 1-6, every other input will cancel!)")
                        for pokémon in player.list_pokémon:
                            print(pokémon)
                        answer = int(input())
                        # If
                        # 1.the user has input a number 
                        # 2 is between 1 and 6
                        # we cal use_potion. this method has a bool return to verify it's executed or not. 
                        if type(answer) == int:
                            if answer >=1 and answer <7:
                                # If use_potion has healed a pokémon, we break from the loop.
                                if use_potion(formatted_input,player.list_pokémon[answer - 1]):
                                    break
                        # if the input isn't a number, we consider it a cancel and so we break from the loop.
                        else:
                            break
            # If the input is Cancel: self explanatory.
            elif formatted_input == "Cancel":
                pass
            else:
                print("Invalid input! Try again")
        
        # entry point of the  use_item method!
        print(self)
        user_input = input("Enter the object you want to use: ")
        dict_selector(user_input)


