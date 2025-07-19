from Classes import *
from Classes.pokemon import Pokémon
from Classes.shop import Shop
from Classes.trainer import Trainer, Player
from Classes.battle import battle

player = Player("bouffion",list_pokémon = [Pokémon(pok_id= 2), Pokémon(pok_id= 4), Pokémon(pok_id= 7), Pokémon(pok_id= 25), Pokémon(pok_id= 25), Pokémon(pok_id= 151,level= 40)])
print(player.is_player)
trainer = Trainer("Regis",[Pokémon(pok_id= 1,level= 3)])
player.inventory.update_inventory(item= 'Poké Ball',quantity= 5)
player.inventory.update_inventory(item= 'Potion',quantity= 5)
player.inventory.update_inventory(item= 'Hyper Potion',quantity= 2)
player.inventory.update_inventory(item= 'Pierre Foudre',quantity= 1)
player.inventory.add_badge_and_no_duplicate('Boulder Badge')
#battle(player= player, opponent= trainer)
#battle(player= player, opponent= trainer)
test_shop = Shop("Max","Argenta")
test_shop.shop(player)
player.use_item()
pok1 = Pokémon(50,True,5)
battle(player,pok1)
print(player)

