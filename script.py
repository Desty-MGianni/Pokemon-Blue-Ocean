from Classes import *
from Classes.pokemon import Pokémon
from Classes.trainer import Trainer, Player
from Classes.battle import battle
from Classes.city import City





player = Player("bouffion",list_pokémon = [Pokémon(pok_id= 2), Pokémon(pok_id= 4), Pokémon(pok_id= 7), Pokémon(pok_id= 25), Pokémon(pok_id= 25), Pokémon(pok_id= 151,level= 40)])
print(player.is_player)
trainer = Trainer("Regis",[Pokémon(pok_id= 1,level= 3)])
player.inventory.update_inventory(item= 'Poké Ball',quantity= 5)
player.inventory.update_inventory(item= 'Potion',quantity= 5)
player.inventory.update_inventory(item= 'Hyper Potion',quantity= 2)
player.inventory.update_inventory(item= 'Pierre Foudre',quantity= 1)
#battle(player= player, opponent= trainer)
#battle(player= player, opponent= trainer)
argenta = City(
    name= 'Argenta',
    has_arena= True, 
    shop_rank= "Beginner",
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
            name= 'Pierre',
            list_pokémon= [
                Pokémon(pok_id= 43,level= 13), 
                Pokémon(pok_id= 67,level= 15)]),
        "Nom Badge": 'Boulder Badge'},)

argenta.roaming(player= player)
player.use_item()
pok1 = Pokémon(50,True,5)
battle(player,pok1)
print(player)

