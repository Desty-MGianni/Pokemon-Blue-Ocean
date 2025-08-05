from time import sleep
from Classes.clearscreen import clearscreen
from Classes.inventory import Inventory
from Classes. menu import Menu
from Classes.pokemon import Pokémon
from Classes.trainer import Trainer, Player
from Classes.battle import battle
from Classes.city import City, End, Bourg_palette
from Classes.road import Road
from Classes.site import Site



argenta = City(
    name= 'Argenta',
    has_arena= True, 
    shop_rank= "Beginner",
    arena_info= {
        "Name": "Arène d'Argenta", 
        "Liste Dresseurs": [
            Trainer(
                name= 'Sous-champion 1', 
                list_pokémon= [Pokémon(pok_id= 30)]), 
            Trainer(
                name= 'Sous-champion 2', 
                list_pokémon= [Pokémon(pok_id= 53)])],
        "Champion": Trainer(
            name= 'Pierre',
            list_pokémon= [
                Pokémon(pok_id= 43,level= 13), 
                Pokémon(pok_id= 67,level= 15)]),
        "Nom Badge": 'Boulder Badge'}
)
jadielle = City(
    name= 'Jadielle',
    has_arena= True, 
    shop_rank= "Beginner",
    arena_info= {
        "Name": "Arène de Jadielle", 
        "Liste Dresseurs": [
            Trainer(
                name= 'Sous-champion 1', 
                list_pokémon= [Pokémon(pok_id= 30)]), 
            Trainer(
                name= 'Sous-champion 2', 
                list_pokémon= [Pokémon(pok_id= 53)])],
        "Champion": Trainer(
            name= 'Giovanni',
            list_pokémon= [
                Pokémon(pok_id= 43,level= 13), 
                Pokémon(pok_id= 67,level= 15)]),
        "Nom Badge": 'Earth Badge'}
)
azuria = City(
        name= 'Azuria',
    has_arena= True, 
    shop_rank= "Beginner",
    arena_info= {
        "Name": "Arène d'Azuria", 
        "Liste Dresseurs": [
            Trainer(
                name= 'Sous-champion 1', 
                list_pokémon= [Pokémon(pok_id= 30)]), 
            Trainer(
                name= 'Sous-champion 2', 
                list_pokémon= [Pokémon(pok_id= 53)])],
        "Champion": Trainer(
            name= 'Ondine',
            list_pokémon= [
                Pokémon(pok_id= 43,level= 13), 
                Pokémon(pok_id= 67,level= 15)]),
        "Nom Badge": 'Cascade Badge'}
)
safrania = City(
    name= 'Safrania',
    has_arena= True, 
    shop_rank= "Intermediate",
    arena_info= {
        "Name": "Arène de Safrania", 
        "Liste Dresseurs": [
            Trainer(
                name= 'Sous-champion 1', 
                list_pokémon= [Pokémon(pok_id= 30)]), 
            Trainer(
                name= 'Sous-champion 2', 
                list_pokémon= [Pokémon(pok_id= 53)])],
        "Champion": Trainer(
            name= 'Morgane',
            list_pokémon= [
                Pokémon(pok_id= 43,level= 13), 
                Pokémon(pok_id= 67,level= 15)]),
        "Nom Badge": 'Marsh Badge'}
)
lavanvile = City(
    name= 'Lavanvile',
    has_arena= False, 
    shop_rank= "Intermediate",
    arena_info= None
)
céladopole = City(
    name= 'Céladopole',
    has_arena= True, 
    shop_rank= "Advanced",
    arena_info= {
        "Name": "Arène d'argenta", 
        "Liste Dresseurs": [
            Trainer(
                name= 'Sous-champion 1', 
                list_pokémon= [Pokémon(pok_id= 30)]), 
            Trainer(
                name= 'Sous-champion 2', 
                list_pokémon= [Pokémon(pok_id= 53)])],
        "Champion": Trainer(
            name= 'Erika',
            list_pokémon= [
                Pokémon(pok_id= 43,level= 13), 
                Pokémon(pok_id= 67,level= 15)]),
        "Nom Badge": 'Rainbow Badge'}
)
carmin_sur_mer = City(
    name= 'Carmin sur Mer',
    has_arena= True, 
    shop_rank= "Intermediate",
    arena_info= {
        "Name": "Arène de Carmin sur Mer", 
        "Liste Dresseurs": [
            Trainer(
                name= 'Sous-champion 1', 
                list_pokémon= [Pokémon(pok_id= 30)]), 
            Trainer(
                name= 'Sous-champion 2', 
                list_pokémon= [Pokémon(pok_id= 53)])],
        "Champion": Trainer(
            name= 'Major Bob',
            list_pokémon= [
                Pokémon(pok_id= 43,level= 13), 
                Pokémon(pok_id= 67,level= 15)]),
        "Nom Badge": 'Thunder Badge'}
)
parmanie = City(
    name= 'Parmanie',
    has_arena= True, 
    shop_rank= "Advanced",
    arena_info= {
        "Name": "Arène de Parmanie", 
        "Liste Dresseurs": [
            Trainer(
                name= 'Sous-champion 1', 
                list_pokémon= [Pokémon(pok_id= 30)]), 
            Trainer(
                name= 'Sous-champion 2', 
                list_pokémon= [Pokémon(pok_id= 53)])],
        "Champion": Trainer(
            name= 'Koga',
            list_pokémon= [
                Pokémon(pok_id= 43,level= 13), 
                Pokémon(pok_id= 67,level= 15)]),
        "Nom Badge": 'Soul Badge'}
)
cramois_ile = City(
    name= "Cramois'île",
    has_arena= True, 
    shop_rank= "Max",
    arena_info= {
        "Name": "Arène d'argenta", 
        "Liste Dresseurs": [
            Trainer(
                name= 'Sous-champion 1', 
                list_pokémon= [Pokémon(pok_id= 30)]), 
            Trainer(
                name= 'Sous-champion 2', 
                list_pokémon= [Pokémon(pok_id= 53)])],
        "Champion": Trainer(
            name= 'Auguste',
            list_pokémon= [
                Pokémon(pok_id= 43,level= 13), 
                Pokémon(pok_id= 67,level= 15)]),
        "Nom Badge": 'Volcano Badge'}
)

plateau_indigo = End()
bourg_palette = Bourg_palette()

foret_de_jade = Site(name= "Foret de Jade")
mont_selenite = Site(name= "Mont Sélénite")
grotte_azurée = Site(name= "Grotte Azurée")
tour_pokémon = Site(name= "Tour Pokémon")
cave_taupiqueur = Site(name= "Cave Taupiqueur")
iles_écumes = Site(name= "îles Écumes")
parc_safari = Site(name= "Parc Safari")
centrale_electrique = Site(name= "Centrale")
grotte = Site(name= "Grotte")
manoir_pokémon = Site(name= "Manoir Pokémon")
route_victoire = Site(name= "Route Victoire")

road_1 = Road(name= "Route 1")
road_2 = Road(name= "Route 2")
road_3 = Road(name= "Route 3")
road_4 = Road(name= "Route 4")
road_5 = Road(name= "Route 5")
road_6 = Road(name= "Route 6")
road_7 = Road(name= "Route 7")
road_8 = Road(name= "Route 8")
road_9 = Road(name= "Route 9")
road_10 = Road(name= "Route 10")
road_11 = Road(name= "Route 11")
road_12 = Road(name= "Route 12")
road_13 = Road(name= "Route 13")
road_14 = Road(name= "Route 14")
road_15 = Road(name= "Route 15")
road_16 = Road(name= "Route 16")
road_17 = Road(name= "Route 17")
road_18 = Road(name= "Route 18")
road_19 = Road(name= "Route 19")
road_20 = Road(name= "Route 20")
road_21 = Road(name= "Route 21")
road_22 = Road(name= "Route 22")
road_23 = Road(name= "Route 23")
road_24 = Road(name= "Route 24")
road_25 = Road(name= "Route 25")
azuria_to_carmin = Road(name="Chemin express Azuria/Carmin sur Mer")


relation_map_dict = {
    bourg_palette: [road_1, road_21],
    jadielle: [road_2, road_22, road_1],
    foret_de_jade: [argenta, road_2],
    argenta: [road_3, foret_de_jade],
    mont_selenite: [road_4, road_3], 
    azuria: [road_5, road_9, road_24],
    azuria_to_carmin: [road_5, road_6],
    carmin_sur_mer: [road_11, road_6],
    safrania: [road_5, road_6, road_7, road_8],
    grotte: [road_10, road_9],
    lavanvile: [tour_pokémon, road_8, road_12],
    tour_pokémon: [lavanvile],
    cave_taupiqueur: [foret_de_jade],
    parmanie: [parc_safari, road_18, road_19, road_15],
    parc_safari: [parmanie],
    céladopole: [road_16, road_7],
    iles_écumes: [road_20, road_19],
    cramois_ile: [manoir_pokémon, road_21, road_20],
    route_victoire: [plateau_indigo, road_23],
    plateau_indigo: [route_victoire],
    road_1: [jadielle, bourg_palette],
    road_2: [foret_de_jade, jadielle],
    road_3: [mont_selenite, argenta],
    road_4: [azuria, mont_selenite],
    road_5: [safrania, azuria_to_carmin, azuria],
    road_6: [carmin_sur_mer, azuria_to_carmin, safrania],
    road_7: [céladopole, safrania],
    road_8: [lavanvile, safrania],
    road_9: [grotte, azuria],
    road_10: [lavanvile, grotte],
    road_11: [cave_taupiqueur, road_12, carmin_sur_mer],
    road_12: [road_13, road_11, lavanvile],
    road_13: [road_14, road_12],
    road_14: [road_15, road_13],
    road_15: [parmanie, road_14],
    road_16: [road_17, céladopole],
    road_17: [road_18, road_16],
    road_18: [parmanie, road_17],
    road_19: [iles_écumes, parmanie],
    road_20: [cramois_ile, iles_écumes],
    road_21: [bourg_palette, cramois_ile],
    road_22: [road_23, jadielle],
    road_23: [route_victoire, road_22],
    road_24: [road_25, grotte_azurée, azuria],
    road_25: [road_24],
    }

def creation_player():
    print("Hello and welcome to my Python made Pokémon 1st generation!")
    sleep(2)
    print("First of all, you need a name!")
    sleep(1)
    name = input("What is your character's name?\n")
    sleep(1)
    bulbizarre = Pokémon(pok_id= 1,level= 5)
    salamèche = Pokémon(pok_id= 4, level= 5)
    carapuce = Pokémon(pok_id= 7, level=5)
    while True:
        clearscreen()
        print(f"Ok, {name}, now you need to choose your Pokémon starter!")
        print(f"\t1 | {bulbizarre.name}, {bulbizarre.type}\n" 
            f"\t2 | {salamèche.name}, {salamèche.type}\n" 
            f"\t3 | {carapuce.name}, {carapuce.type}\n"
            )
        starter_choice = ''
        sleep(1)
        try:
            starter_choice = int(input("Enter the corresponding number: "))
        except ValueError:
            starter_choice = 0
        match starter_choice:
            case 1:
                print(f"You chose {bulbizarre.name}")
                sleep(2)
                return Player(name= name, list_pokémon=[bulbizarre])
            case 2:
                print(f"You chose {salamèche.name}")
                sleep(2)
                return Player(name= name, list_pokémon= [salamèche])
            case 3:
                print(f"You chose {carapuce.name}")
                sleep(2)
                return Player(name= name, list_pokémon= [carapuce])
            case _:
                continue

def where_to_go(position):
    while True:
        counter = 1
        print("Destination available: ")
        for destination in relation_map_dict[position]:
            print(f"{counter}| {destination.name}")
            counter += 1
        choice = input("Enter the number corespondint where you want to go or type 'c' to cancel : ")
        if choice == "cancel" or choice == "c":
            return position
        try:
            choice_int = int(choice)
        except ValueError:
            continue
        if choice_int > 0 and choice_int < len(relation_map_dict[position]):
            return relation_map_dict[position][choice_int - 1]

def game_loop():
    where_i_am = argenta
    while True:
        where_i_am.roaming(player= player)
        where_i_am = where_to_go(position= where_i_am)

                


clearscreen()
player = creation_player()
game_loop()
print(player.is_player)
trainer = Trainer("Regis",[Pokémon(pok_id= 1,level= 3)])
player.inventory.update_inventory(item= 'Poké Ball',quantity= 5)
player.inventory.update_inventory(item= 'Potion',quantity= 5)
player.inventory.update_inventory(item= 'Hyper Potion',quantity= 2)
player.inventory.update_inventory(item= 'Pierre Foudre',quantity= 1)
player.inventory.add_pok_pc(pokemon= Pokémon(pok_id=34,level= 5))
player.inventory.add_pok_pc(pokemon= Pokémon(pok_id=135,level= 5))
#battle(player= player, opponent= trainer)
#battle(player= player, opponent= trainer)
plateau_indigo.roaming(player= player)
player.use_item()
pok1 = Pokémon(50,True,5)
battle(player,pok1)
print(player)


