import random
import math
import csv
from time import sleep

class Pokémon:
    # Functin dant load csv file with experience needed to level up and converting it to int: int format dict
    def load_exp_table():
        with open('evo_exp_tables/exp_table.csv', newline='') as exp_table:
            temp = dict(csv.reader(exp_table,delimiter=';'))
            converted = {int(lvl): int(exp) for lvl, exp in temp.items()}
        return converted
    
    # Function that load a evolution by level table and convert it to the right format like exp_table
    def load_evo_lvl_table():
        with open('Evo_exp_tables/evolution_lvl.csv',newline='') as evo_table:
            temp = list(csv.reader(evo_table,delimiter=';'))
            converted = {int(prevo_id): [int(evo_id), int(level)] for prevo_id, evo_id, level in temp}
        return converted
    
    # Creating a Dict with ID as key, Name and Type as Values
    # Every line is a evolution line.
    pok_table = {
       1: ["Bulbizarre", ["Plante", "Poison"]], 2: ["Herbizarre", ["Plante", "Poison"]], 3: ["Florizarre", ["Plante", "Poison"]],
       4: ["Salamèche", ["Feu"]], 5: ["Reptincel", ["Feu"]], 6: ["Dracaufeu", ["Feu", "Vol"]],
       7: ["Carapuce", ["Eau"]], 8: ["Carabaffe", ["Eau"]], 9: ["Tortank", ["Eau"]],
       10: ["Chenipan", ["Insecte"]], 11: ["Chrysacier", ["Insecte"]], 12: ["Papilusion", ["Insecte", "Vol"]],
       13: ["Aspicot", ["Insecte", "Poison"]], 14: ["Coconfort", ["Insecte", "Poison"]], 15: ["Dardargnan", ["Insecte", "Poison"]],
       16: ["Roucool", ["Normal", "Vol"]], 17: ["Roucoups",["Normal", "Vol"]], 18: ["Roucarnage", ["Normal", "Vol"]],
       19: ["Rattata", ["Normal"]], 20: ["Rattatac", ["Normal"]],
       21: ["Piafabec", ["Normal", "Vol"]], 22: ["Rapasdepic", ["Normal", "Vol"]],
       23: ["Abo", ["Poison"]], 24: ["Arbok", ["Poison"]],
       25: ["Pikachu", ["Éléctrik"]], 26: ["Raichu", ["Éléctrik"]],
       27: ["Sabelette", ["Sol"]], 28: ["Sablaireau", ["Sol"]],
       29: ["Nidoran ♀", ["Poison"]], 30: ["Nidorina", ["Poison"]], 31: ["Nidoqueen", ["Poison", "Sol"]],
       32: ["Nidoran ♂", ["Poison"]], 33: ["Nidorino", ["Poison"]], 34: ["Nidoking", ["Poison", "Sol"]],
       35: ["Mélofée", ["Fée"]], 36: ["Mélodelfe", ["Fée"]],
       37: ["Goupix", ["Feu"]], 38: ["Feunard", ["Feu"]],
       39: ["Rondoudou", ["Normal", "Fée"]], 40: ["Grodoudou", ["Normal", "Fée"]],
       41: ["Nosferapti", ["Poion", "Vol"]], 42: ["Nosferalto", ["Poison", "Vol"]],
       43: ["Mystherbe", ["Plante", "Poison"]], 44: ["Ortide", ["Plante", "Poison"]], 45: ["Raflfleisia", ["Plante", "Poison"]],
       46: ["Paras", ["Insecte", "Plante"]], 47: ["Parasect", ["Insecte", "Plante"]],
       48: ["Mimitoss", ["Insecte", "Poison"]], 49: ["Aéromite", ["Insecte", "Poison"]],
       50: ["Taupiqueur", ["Sol"]], 51: ["Triopikeur", ["Sol"]],
       52: ["Miaouss", ["Normal"]], 53: ["Persian", ["Normal"]],
       54: ["Psykokwak", ["Eau"]], 55: ["Akwakwak", ["Eau"]],
       56: ["Férosinge", ["Combat"]], 57: ["Colossinge", ["Combat"]],
       58: ["Caninos", ["Feu"]], 59: ["Arcanin", ["Feu"]],
       60: ["Ptitard", ["Eau"]], 61: ["Tétarte", ["Eau"]], 62: ["Tartard", ["Eau", "Combat"]],
       63: ["Abra", ["Psy"]], 64: ["Kadabra", ["Psy"]], 65: ["Alakazam", ["Psy"]],
       66: ["Machoc", ["combat"]], 67: ["Machopeur", ["Combat"]], 68: ["Mackogneur", ["Combat"]],
       69: ["Chétiflor", ["Plante", "Poison"]], 70: ["Boustiflor", ["Plante", "Poison"]], 71: ["Empiflor", ["Plante", "Poison"]],
       72: ["Tentacool", ["Eau", "Poison"]], 73: ["Tentacruel", ["Eau", "Poison"]],
       74: ["Racaillou", ["Roche", "Sol"]], 75: ["Gravalanch", ["Roche", "Sol"]], 76: ["Grolem", ["Roche", "Sol"]],
       77: ["Ponyta", ["Feu"]], 78: ["Galopa", ["Feu"]],
       79: ["Ramoloss", ["Eau", "Psy"]], 80: ["Flagadoss", ["Eau", "Psy"]],
       81: ["Magnéti", ["Éléctrik", "Acier"]], 82: ["Magnétorn", ["Éléctrik", "Acier"]],
       83: ["Canarticho", ["Normal", "Vol"]],
       84: ["Doduo", ["Normal", "Vol"]], 85: ["Dodrio", ["Normal", "Vol"]],
       86: ["Otaria", ["Eau"]], 87: ["Lamantine", ["Eau", "Glace"]],
       88: ["Tadmorv", ["Poison"]], 89: ["Grotadmorv", ["Poison"]],
       90: ["Kokyas", ["Eau"]], 91: ["Crustabri", ["Eau", "Glace"]],
       92: ["Fanominus", ["Spectre", "Poison"]], 93: ["Spectrum", ["Spectre", "Poison"]], 94: ["Ectoplasma", ["Spectre", "Poison"]],
       95: ["Onix", ["Roche", "Sol"]],
       96: ["Soporifik", ["Psy"]], 97: ["Hypnomade", ["Psy"]],
       98: ["Krabby", ["Eau"]], 99: ["Krabboss", ["Eau"]],
       100: ["Voltorbe", ["Éléctrik"]], 101: ["Électrode", ["Éléctrik"]],
       102: ["Noeunoeuf", ["Plante", "Psy"]], 103: ["Noadkoko", ["Plante", "Psy"]],
       104: ["Osselait", ["Sol"]], 105: ["Ossatueur", ["Sol"]],
       106: ["Kicklee", ["Combat"]],
       107: ["Tygnon", ["combat"]],
       108: ["Excelangue", ["Normal"]],
       109: ["Smogo", ["Poison"]], 110: ["Smogogo", ["Poison"]],
       111: ["Rhinocorne", ["Sol", "Roche"]], 112: ["Rhinoféros", ["Sol", "Roche"]],
       113: ["Leveinard", ["Normal"]],
       114: ["Saquedeneu", ["Plante"]],
       115: ["Kangourex", ["Normal"]],
       116: ["Hypotrempe", ["Eau"]],
       117: ["Hypocéan", ["Eau"]],
       118: ["Poissirène", ["Eau"]], 119: ["Poissoroy", ["Eau"]],
       120: ["Stari", ["Eau"]], 121: ["Staross", ["Eau", "Psy"]],
       122: ["M. Mime", ["Psy", "Fée"]],
       123: ["Insécateur", ["Insecte", "Vol"]],
       124: ["Lipoutou", ["Glace", "Psy"]],
       125: ["Élektek", ["Électrik"]],
       126: ["Magmar", ["Feu"]],
       127: ["Scarabrute", ["Insecte"]],
       128: ["Tauros", ["Normal"]],
       129: ["Magicarpe", ["Eau"]], 130: ["Léviator", ["Eau", "Vol"]],
       131: ["Lokhlass", ["Eau", "Glace"]],
       132: ["Méthamorph", ["Normal"]],
       133: ["Évoli", ["Normal"]], 134: ["Aquali", ["Eau"]], 135: ["Voltali", ["Électrik"]], 136: ["Pyroli", ["Feu"]],
       137: ["Porygon", ["Normal"]],
       138: ["Amonita", ["Roche", "Eau"]], 139: ["Amonistar", ["Roche", "Eau"]],
       140: ["Kabuto", ["Roche", "Eau"]], 141: ["Kabutops", ["Roche", "Eau"]],
       142: ["Ptéra", ["Roche", "Vol"]],
       143: ["Ronflex", ["Normal"]],
       144: ["Artikodin", ["Glace", "Vol"]],
       145: ["Électhor", ["Éléctrik", "Vol"]],
       146: ["Sulfura", ["Feu", "Vol"]],
       147: ["Minidraco", ["Dragon"]], 148: ["Draco", ["Dragon"]], 149: ["Dracolosse", ["Dragon", "Vol"]],
       150: ["Mewtwo", ["Psy"]],
       151: ["Mew", ["Psy"]]
       } 
    
    # Creaing an evolution_stone_table becaue the architecture needed (becaue of pokemon eevie) was convoluted and not possible(with my little knowledge) with csv imports.
    # Keys are str, values are dicts of int keys and int values, keys are the pok_id, values are the evo_id like evolution_lvl_table
    evolution_stone_table = {
        'Pierre Eau': {61: 62, 90: 91, 120: 121, 133: 134},
        'Pierre Feu': {37: 38, 58: 59, 133: 136},
        'Pierre Feuille': {44: 45, 70: 71, 102: 103},
        'Pierre Foudre': {25: 26, 133: 135},
        'Pierre Lune': {30: 31, 33: 34, 35: 36, 39: 40}
    }
    # store the result of loading evo_lvl.csv
    evolution_lvl_table = load_evo_lvl_table()
    
    # store the result of loading exp_table.csv
    exp_table = load_exp_table()

    # Consctructor
    def __init__(self, pok_id: int, is_wild: bool = False, level: int = 3):
        self.pok_id = pok_id
        self.name = self.set_name()
        self.level = level
        self.exp = 0
        self.max_health = 25 + random.randint(3,5) * self.level
        self.health = self.max_health
        self.type = self.pok_table[pok_id][1]
        self.is_wild = is_wild
        self.is_ko = False
        self.determ_is_evolvable()
        self.private_id = random.randint(1000000,10000000)
   
    # ToString method that display the basic info of the pokémon.
    def __repr__(self):
         return f"{self.name} is a lvl {self.level} {Pokémon.pok_table[self.pok_id][0]} with {self.health}/{self.max_health} HP"
    
    # Method that search the name of the pokemon from it's key in the dic ref_table
    def set_name(self):
        return Pokémon.pok_table[self.pok_id][0]
   
    # Method that ask user input to change the name of the pokémon
    def change_name(self):
        temp = input("What Type the new name of the Pokémon: ")
        if temp != "":
             self.name = temp
   
    # Method that increase the lvl of the pokémon, increasing it's HP and printing it to console.
    def level_up(self):
        self.level += 1
        temp = random.randint(3,5)
        self.max_health += temp
        print(f"{self.name} has leveled up to {self.level}! (HP + {temp})")

    # Method that increase exp and call a check_level_up function
    def gain_exp(self, enemy_level: int):
        base = random.randint(1,3)
        full = math.floor(base * (enemy_level**2.5) + base * self.level/4)
        self.exp += full
        print(f"{self.name} gained {full} experience points!")
        self.check_level_up()
    
    # Method that verify if the amount of exp exceed the limit set in exp_table to trigger a level up.
    def check_level_up(self):
        while self.exp >= Pokémon.exp_table[self.level]:
            self.exp -= Pokémon.exp_table[self.level]          
            self.level_up()
            self.determ_is_evolvable()
            if self.is_evolvable:
                self.check_level_evolution()

    # Method that check if the pok_id is a key in either evolution stone table or evolution_lvl_table
    def determ_is_evolvable(self):
        if self.pok_id in Pokémon.evolution_lvl_table.keys():
            self.is_evolvable = True
        else:
            for lis in Pokémon.evolution_stone_table.values():
                if self.pok_id in lis:
                    self.is_evolvable = True
                    break
                else:
                    self.is_evolvable = False
    
    # Method that will be called during level_ups to verify if the level threshold is cossed and to will trigger evolution
    def check_level_evolution(self):
        if self.is_evolvable:
            if self.level >= Pokémon.evolution_lvl_table[self.pok_id][1]:
                sleep(0.5)
                print("\t.")
                sleep(1)
                print("\t.")
                sleep(1)
                print("\t.")

                print(f"Congratulaton! {self.name} has evolved from {Pokémon.pok_table[self.pok_id][0]} to ", end='')
                self.pok_id = Pokémon.evolution_lvl_table[self.pok_id][0]
                print(f"{Pokémon.pok_table[self.pok_id][0]}")
                self.max_health += random.randint(40,50)
                self.name = self.set_name()

    # Method that handle the verification of ID's and, if ok, proceed to evolve the pokémon.      
    def check_stone_evolution(self, stone: str):
        if self.is_evolvable:
            if self.pok_id in Pokémon.evolution_stone_table[stone]:
                answer = input(f"{self} can be evolved with {stone}. Do you want to proceed ?")
                if answer == "yes" or answer == "y":
                    sleep(0.5)
                    print("\t.")
                    sleep(1)
                    print("\t.")
                    sleep(1)
                    print("\t.")
                    print(f"Congratulaton! {self.name} has evolved from {Pokémon.pok_table[self.pok_id][0]} to ", end='')
                    self.pok_id = Pokémon.evolution_stone_table[stone][self.pok_id]
                    print(f"{Pokémon.pok_table[self.pok_id][0]}")
                    self.max_health += random.randint(40,50)
                    self.name = self.set_name()
                    return True
        return False

    # Method that set is_ko to true if the instance has no HP left
    def check_knocked_out(self):
        if self.health <=0:
            self.health = 0
            self.is_ko = True
            print(f"{self.name} is K.O! He cannot continue to fight")
    
    # Method that reduce the health of a pokemon and check if is_knoced_out
    def lose_health(self,damages):
        self.health -= damages
        self.check_knocked_out()
    
    # Method that handle healing the pokémon, with potions or pokëmon center!
    def gain_health(self,heal):
        pre_heal = self.health
        self.health += heal
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regained {self.health - pre_heal} HP")
    
    # method that return a int value corresponding to the damage inflicted to à pokémon
    def pok_damages(self):
        return math.floor(self.max_health * 0.25 + random.randint(0,3))

    