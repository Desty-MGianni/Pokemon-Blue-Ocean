from pprint import pprint
from Classes import (
    battle,
    pokemon as pok, 
    trainer as t,

)
player = t.Trainer("bouffion",list_pokémon=[pok.Pokémon(2),pok.Pokémon(4),pok.Pokémon(7),pok.Pokémon(25),pok.Pokémon(25),pok.Pokémon(151,level= 40)])
player.create_player()
print(player.is_player)
trainer = t.Trainer("Regis",[pok.Pokémon(1)])
player.inventory.add_inventory('Super Ball',3)
player.inventory.add_inventory('Potion',5)
player.inventory.add_inventory('Hyper Potion',2)
player.inventory.add_inventory('Pierre Foudre',2)
battle(player,trainer)
player.inventory.add_badge_and_no_duplicate('Boulder Badge')
player.inventory.use_item(False,False,player,False)
pok1 = pok.Pokémon(50,True,5)
battle(player,pok1)
print(player)
