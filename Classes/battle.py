import random
from time import sleep
from Classes import (
    trainer as t,
    pokemon as p,
)
# function that handle every battle in the game, proceed to check if it's a trainer or a wild pokémon.
def battle(player:t.Trainer, opponent):
    # Nested function that handle the attack from a pokémon to another. pok_one is always the attacking pokémon.
    # So in the calling, if we want the opponent to attack, pok_one has to be the opponent pokémon.
    def attack(pok_one: p.Pokémon,pok_two:p.Pokémon):
        damages = pok_one.pok_damages()
        print(f"{pok_one.name} launch an attack!")
        sleep(1)
        print(f"{pok_one.name} has inflicted {damages} to {pok_two.name}!")
        pok_two.lose_health(damages)
        sleep(1)
    # nested function that handle trainer vs trainer battle.
    def battle_trainer(player:t.Trainer, opponent:t.Trainer):
        player_all_pok_ko = player.check_all_pok_ko()
        trainer_all_pok_ko = False
        # Maybe need to change 
        if player_all_pok_ko:
            print("You can't engage in battle when all your pokémon are K.O!")
        else:
            print(f"{opponent.name} choose {opponent.list_pokémon[0].name}!")
            sleep(1)
            print(f"{player.list_pokémon[0].name}, Go!")
            # Entering the battle loop with the 4 choices
            while (not player_all_pok_ko and not trainer_all_pok_ko):
                print(f"\n\tOpponent: {opponent.list_pokémon[0]}")
                print(f"\tPlayer: {player.list_pokémon[0]}\n")
                option = input("What option do you want to do:\n" \
                    "\t1: Attack\n" \
                    "\t2: Use Object\n" \
                    "\t3: Change Pokémon\n" \
                    "\t4: Flee\n"
                )

                match option:
                    case '1'| 'Attack'| 'attack':
                        if not player.list_pokémon[0].is_ko:
                            attack(player.list_pokémon[0],opponent.list_pokémon[0])
                            if opponent.list_pokémon[0].is_ko:
                                player.list_pokémon[0].gain_exp(opponent.list_pokémon[0].level)
                                trainer_all_pok_ko = opponent.check_all_pok_ko()
                        else:
                            print(f"Your {player.list_pokémon[0].name} is K.O, He's unable to fight!")
                            continue
                    case '2'| 'use object'| 'Use Object':
                        player.inventory.use_item(True,False,player, opponent)
                    case '3'| 'Change Pokémon'| 'change'| 'change pokémon':
                        player.change_pokemon()
                    case '4'| 'Flee'| 'flee':
                        print('You can\'t escape in a battle versus a trainer!')
                        continue
                    case _:
                        print('Invalid input! Try again') 
                
                if opponent.list_pokémon[0].is_ko:
                    if not trainer_all_pok_ko:
                        opponent.change_pokemon()
                        continue
                    else:
                        break
                else:
                    if player.list_pokémon[0].is_ko:
                        continue
                    else:
                        attack(opponent.list_pokémon[0],player.list_pokémon[0])
                
            if player_all_pok_ko == False:
                print("You won the fight!")
                money_gained = random.randint(1250,3600)
                print(f"You have won {money_gained} Poké-Dollars!")
                player.inventory.manage_money(money_gained)
                
            else:
                print("You have lost the fight!")
                money_lost = random.randint(-1250,-3600)
                print(f"You have lost {abs(money_lost)} Poké-Dollars!")
                player.inventory.manage_money(money_lost)

    # Nested function that handle a battle vs a wild pokémon, wich we can capture.
    def battle_pokémon(player:t.Trainer, opponent:p.Pokémon):
        player_all_pok_ko = player.check_all_pok_ko()
        if not player_all_pok_ko:
            sleep(1)
            print(f"{player.list_pokémon[0].name}, Go!")
            while not opponent.is_ko or not player_all_pok_ko:
                print(f"\n\tOpponent: {opponent}")
                print(f"\tPlayer: {player.list_pokémon[0]}\n")
                option = input("What option do you want to do:\n" \
                    "\t1: Attack\n" \
                    "\t2: Use Object\n" \
                    "\t3: Change Pokémon\n" \
                    "\t4: Flee\n"
                )
                
                match option:
                    case '1'| 'Attack'| 'attack':
                        if not player.list_pokémon[0].is_ko:
                            attack(player.list_pokémon[0],opponent)
                            if opponent.is_ko:
                                player.list_pokémon[0].gain_exp(opponent.level)
                                break
                        else:
                            print(f"Your {player.list_pokémon[0].name} is K.O, He's unable to fight!")
                            continue
                    case '2'| 'use object'| 'Use Object':
                        player.inventory.use_item(True,True,player,opponent)
                        if opponent.is_wild == False:
                            break
                    case '3'| 'Change Pokémon'| 'change'| 'change pokémon':
                        player.change_pokemon()
                    case '4'| 'Flee'| 'flee':
                        if player.list_pokémon[0].is_ko:
                            print("You can't escape with your pokémon KO, change your Pokémon!")
                            continue
                        rng = random.randint(0,10)
                        if rng <= 7:
                            print("You managed to escape!")
                            break
                        else:
                            print("You failed to escape!")
                    case _:
                        print('Invalid input! Try again')
                        continue
                
                if not opponent.is_ko and not player.list_pokémon[0].is_ko:
                    attack(opponent,player.list_pokémon[0])
                else:
                    continue
                player_all_pok_ko = player.check_all_pok_ko()
                
            if player_all_pok_ko == True:
                print("You have lost the fight!")

    
    # Here is the entry point of the battle function, we detect if the opponent is a trainer or a wild pokémon
    battle_intro_message = f"\nYou have entered a battle versus "
    match type(opponent):
        case t.Trainer:
            battle_intro_message += f"{opponent.name}\n"
            print(battle_intro_message)
            battle_trainer(player,opponent)
        case p.Pokémon:
            battle_intro_message += f"a wild {opponent.name}\n"
            print(battle_intro_message)
            battle_pokémon(player,opponent)
        case _:
            print("Something went wrong in the adver selector")
        
    
    