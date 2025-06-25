from time import sleep
from Classes import (
    trainer as t,
    pokemon as p,
)
# function that handle every battle in the game, proceed to check if it's a trainer or a wild pokémon.
def battle(player:t.Trainer, opponent):   
    # nested function that handle trainer vs trainer battle.         
    def battle_trainer(player:t.Trainer, opponent:t.Trainer):
        player_all_pok_ko = player.check_all_pok_ko()
        trainer_all_pok_ko = False
        # Maybe need to change 
        if player_all_pok_ko:
            print("You can't engage in battle when all your pokémon are K.O!")
        else:
            print(f"{player.list_pokémon[0].name}, Go!")
            # Entering the battle loop with the 4 choices
            while (not player_all_pok_ko and not trainer_all_pok_ko):
                option = input("What option do you want to do:\n" \
                    "1: Attack\n" \
                    "2: Use Object\n" \
                    "3: Change Pokémon\n" \
                    "4: Flee\n"
                )
                match option:
                    case '1'| 'Attack'| 'attack':
                        damages = player.list_pokémon[0].attack()
                        print(f"{player.list_pokémon[0].name} launch an attack!")
                        sleep(1)
                        print(f"{player.list_pokémon[0].name} has inflicted {damages}!")
                        opponent.list_pokémon[0].lose_health(damages)
                        sleep(1)
                        if opponent.list_pokémon[0].is_ko:
                            player.list_pokémon[0].gain_exp(opponent.list_pokémon[0].level)
                    case '2'| 'use object'| 'Use Object':
                        player.inventory.use_item(True,False,player)
                        pass
                    case '3'| 'Change Pokémon'| 'change'| 'change pokémon':
                        print('je suis dans 3')
                        pass
                    case '4'| 'Flee'| 'flee':
                        print('You can\'t escape in a battle versus a trainer!')
                        continue
                    case _:
                        print('Invalid input! Try again') 
                trainer_all_pok_ko = opponent.check_all_pok_ko()
            if player_all_pok_ko == False:
                print("You won the fight!")
            else:
                print("You have lost the fight!")

    # Nested function that handle a battle vs a wild pokémon, wich we can capture.
    def battle_pokémon(player:t.Trainer, opponent:p.Pokémon):
        pass
    # Here is the entry point of the battle function, we detect if the opponent is a trainer or a wild pokémon
    match type(opponent):
        case t.Trainer:
            battle_trainer(player,opponent)
        case p.Pokémon:
            battle_pokémon(player,opponent)
        case _:
            print("Something went wrong in the adver selector")
        
    
    