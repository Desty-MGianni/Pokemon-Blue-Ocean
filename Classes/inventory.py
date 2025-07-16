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
    
    # Method that will handle every dict and every item with nested method
    def use_item(self, in_battle:bool, battle_vs_pok: bool,player ,pokemon):
        
        # Nested method that will compare the input and every object dict.
        def dict_selector(input_str: str):
        
            # Nested method that check if you have an item available in the dictionary.
            def dict_verif_quantity(input_str:str, collec: dict):
                if collec[input_str] > 0:
                    return True
                else:
                    return False
            
            # Nested method that will handle stone evolution.
            def use_stone(input_str: str,player):
                for pokémon in player.list_pokémon:
                    if pokémon.check_stone_evolution(input_str):
                        Inventory.stones[input_str] -= 1
                        if not dict_verif_quantity(input_str,Inventory.stones):
                            break
                    

            # Nested method thatill handle healing pokémon and set value to each potion's health regen
            def use_potion(input_str: str, pokémon: Pokémon):
                if pokémon.health == pokémon.max_health:
                    print("The pokémon selected is full life!")
                    return False
                else:
                    match input_str:
                        case 'Potion':
                            pokémon.gain_health(30)
                            Inventory.potions[input_str] -=1
                        case "Super Potion":
                            pokémon.gain_health(50)
                            Inventory.potions[input_str] -=1
                        case "Hyper Potion":
                            pokémon.gain_health(120)
                            Inventory.potions[input_str] -=1
                        case "Potion Max":
                            pokémon.gain_health(900)
                            Inventory.potions[input_str] -=1
                    return True
                
            def use_revive(input_str: str, pokémon: Pokémon):
                if pokémon.is_ko:
                    pokémon.is_ko = False
                    match input_str:
                        case 'Rappel':
                            pokémon.health = 10
                            Inventory.revives[input_str] -=1
                        case 'Rappel Max':
                            pokémon.health = floor(pokémon.max_health * 0.5)
                            Inventory.revives[input_str] -=1
                    return True
                else:
                    print("Can't use a revive on a pokémon that isn't KO!")
                    return False

            def use_ball(input_str: str, wild_pokémon: Pokémon, player):
                capture_chance = 0
                match input_str:
                    case "Poké Ball":
                        capture_chance = 15
                        Inventory.balls[input_str] -= 1
                    case "Super Ball":
                        capture_chance = 25
                        Inventory.balls[input_str] -= 1
                    case "Hyper Ball":
                        capture_chance = 50
                        Inventory.balls[input_str] -= 1
                    case "Master Ball":
                        capture_chance = 100
                        Inventory.balls[input_str] -= 1
                player.capture_pokemon(wild_pokémon, capture_chance)
            
            # titalised the input to correspond the data in the Dicts.
            formatted_input = input_str.title()
            print(formatted_input)
            
            # Check if input is in balls dict and verify if 
            # 1. bool variable battle_vs_pok is True (as we can only capture pokémons if they're wild)
            # 2. the item is in the inventory by calling dict_verif_quantity 
            # 3. We are in a battle.
            # 4. The pokémon engaged in baattle is not KO
            if formatted_input in Inventory.balls:
                if not in_battle:
                    print("You can't use a Poké Ball outside a battle!")
                if battle_vs_pok:
                    if player.list_pokémon[0].is_ko:
                        print("You can't use a pokéball when your pokémon is KO!")
                    else:
                        if dict_verif_quantity(formatted_input,Inventory.balls):
                            use_ball(input_str= formatted_input,wild_pokémon= pokemon,player= player)
                else:
                    print("You can't capture a pokémon that's already been captured by another trainer.")
            
            # Check if input is in stones dict and verify if
            # 1. bool variable in_battle is False as we don't want to evolve pokémon with stones in a battle.
            # 2. the item is in the inventory by calling dict_verif_quantity
            elif formatted_input in Inventory.stones:
                if not in_battle:
                    if dict_verif_quantity(formatted_input, Inventory.stones):
                        use_stone(formatted_input, player)
                else: 
                    print("You can't use this item in a battle!")
            
            # Check if input is in potion dict and
            # 1 verify if the item is in the inventory
            # we loop so that the player can, if he failed, retry to set wich pokémon he want to heal.
            elif formatted_input in Inventory.potions: 
                if dict_verif_quantity(formatted_input, Inventory.potions):
                    while True:
                        print(F"Which pokémon do you want to use {formatted_input}? (Enter the index of the pokémon. Every other input will cancel!)")
                        counter = 1
                        for pokémon in player.list_pokémon:
                            print(f"{counter}: {pokémon}")
                            counter += 1
                        try:
                            answer = int(input())
                        except ValueError:
                            answer = -1
                        # If
                        # 1.the user has input a number 
                        # 2 is between 1 and 6
                        # we cal use_potion. this method has a bool return to verify it's executed or not. 
                        if answer >=1 and answer <= len(player.list_pokémon):
                            # If use_potion has healed a pokémon, we break from the loop.
                            if use_potion(formatted_input,player.list_pokémon[answer - 1]):
                                break
                        # if the input isn't a number, we consider it a cancel and so we break from the loop.
                        else:
                            break

            elif formatted_input in Inventory.revives:
                if dict_verif_quantity(formatted_input, Inventory.revives):
                    while True:
                        print(F"Which pokémon do you want to use {formatted_input}? (Enter the index of the pokémon. Every other input will cancel!)")
                        counter = 1
                        for pokémon in player.list_pokémon:
                            print(f"{counter}: {pokémon.name}| KO = {pokémon.is_ko}")
                            counter += 1
                        try:
                            answer = int(input())
                        except ValueError:
                            answer = -1
                        # If
                        # 1.the user has input a number 
                        # 2 is between 1 and 6
                        # we cal use_potion. this method has a bool return to verify it's executed or not. 
                        if answer >=1 and answer <= len(player.list_pokémon):
                            # If use_potion has healed a pokémon, we break from the loop.
                            if use_revive(formatted_input,player.list_pokémon[answer - 1]):
                                break
                        else:
                            print("Invalid number!")
                        # if the input isn't a number, we consider it a cancel and so we break from the loop.

            # If the input is Cancel: self explanatory.
            elif formatted_input == "Cancel":
                pass
            else:
                print("Invalid input! Try again")
        
        # entry point of the  use_item method!
        print(self)
        user_input = input("Enter the object you want to use: ")
        dict_selector(user_input)
    
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