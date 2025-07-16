from math import floor
from Classes.pokemon import Pokémon

class Inventory:
    
    def __init__(self):
        self.balls = {'Poké Ball': 0, 'Super Ball': 0, 'Hyper Ball': 0, 'Master Ball': 0}
        self.potions = {'Potion': 0, 'Super Potion': 0, 'Hyper Potion': 0, 'Potion Max': 0}
        self.stones = {'Pierre Feu': 0,'Pierre Eau': 0, 'Pierre Feuille': 0,'Pierre Foudre': 0, 'Pierre Lune': 0}
        self.revives = {'Rappel': 0, 'Rappel Max': 0}
        self.badges = {'Boulder Badge': 0, 'Cascade Badge': 0, 'Thunder Badge': 0, 'Rainbow Badge': 0, 'Soul Badge': 0,'Marsh Badge': 0, 'Volcano Badge': 0, 'Earth Badge': 0}
        self.list_pokemon_pc = []
        self.money = 3000
        pass

    def __repr__(self):
    
        def dict_0_filter(input_dict: dict):
            temp = {}
            for key, value in input_dict.items():
                 if value > 0:
                    temp.update({key: value})
            return temp
          
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
        self.list_pokemon_pc.append(pokemon) 
    

    def add_inventory(self,item: str, quantity: int):
    
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
            match object_name:
                case 'Potion':
                    pokémon.gain_health(30)
                    self.potions[object_name] -=1
                case "Super Potion":
                    pokémon.gain_health(50)
                    self.potions[object_name] -=1
                case "Hyper Potion":
                    pokémon.gain_health(120)
                    self.potions[object_name] -=1
                case "Potion Max":
                    pokémon.gain_health(900)
                    self.potions[object_name] -=1
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
        