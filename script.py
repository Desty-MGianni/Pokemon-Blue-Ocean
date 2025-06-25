
from Classes import (
    battle,
    pokemon as pok, 
    trainer as t,

)

player = t.Trainer("bouffion",list_pokémon=[pok.Pokémon(1),pok.Pokémon(4),pok.Pokémon(7),pok.Pokémon(25)])
player.create_player()
print(player.is_player)
trainer = t.Trainer("Regis",[pok.Pokémon(1)])
print(trainer.list_pokémon)
player.inventory.add_inventory('Super Ball',3)
player.inventory.add_inventory('Potion',5)
player.inventory.add_inventory('Hyper Potion',2)
player.inventory.add_inventory('Pierre Foudre',1)
player.list_pokémon[0].lose_health(20)
battle(player,trainer)
print(player.inventory)
player.inventory.use_item(False,False,player)

