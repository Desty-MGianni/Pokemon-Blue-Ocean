from Classes.pokemon import Pokémon
from Classes.trainer import Trainer, Player
from Classes.battle import battle

player = Player("bouffion",list_pokémon = [Pokémon(pok_id= 2), Pokémon(pok_id= 4), Pokémon(pok_id= 7), Pokémon(pok_id= 25), Pokémon(pok_id= 25), Pokémon(pok_id= 151,level= 40)])
print(player.is_player)
trainer = Trainer("Regis",[Pokémon(1,level= 3)])
player.inventory.add_inventory(item= 'Poké Ball',quantity= 5)
player.inventory.add_inventory('Potion',5)
player.inventory.add_inventory('Hyper Potion',2)
player.inventory.add_inventory('Pierre Foudre',1)
battle(player,trainer)
player.inventory.add_badge_and_no_duplicate('Boulder Badge')
player.use_item()
pok1 = Pokémon(50,True,5)
battle(player,pok1)
print(player)

