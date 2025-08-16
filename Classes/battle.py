import random
from time import sleep
from Classes.clearscreen import clearscreen
from Classes.trainer import Trainer,Player
from Classes.pokemon import Pokémon

# method that handle the battling mechanic with the emblematic 4 choices
def battle(player:Player, opponent: Trainer | Pokémon):
    
    # universal method that is use by player and opponent for dealing damages.
    def deal_damage(pokemon_attacking: Pokémon, pokemon_receiving: Pokémon):
        damages = pokemon_attacking.pok_damages()
        print(f"{pokemon_attacking.name} launch an attack!")
        sleep(1)
        print(f"{pokemon_attacking.name} has inflicted {damages} to {pokemon_receiving.name}!")
        pokemon_receiving.lose_health(damages)
        sleep(1)

    # Method that verify if the parameter is Knocked Out (ONly available for object containing pokémons)
    def check_is_ko(fighter: Pokémon | Trainer):
        if type(fighter) == Pokémon:
            return fighter.is_ko
        elif isinstance(fighter, (Trainer,Player)):
            return fighter.check_all_pok_ko()
    
    # Method that is called in the beginning of a battle.
    def intro_battle():
        sleep(1.5)
        clearscreen()
        intro_message = "You have entered in a battle versus "
        if type(opponent) == Trainer:
            intro_message += f"{opponent.name}"
            print(intro_message)
            sleep(2)
            print(f"{opponent.name} choose {opponent.list_pokémon[0].name}!")
            sleep(1)
        elif type(opponent) == Pokémon:
            intro_message += f"a wild {opponent.name}"
            print(intro_message)
            sleep(1)
        print(f"{player.list_pokémon[0].name}, Go!")
        sleep(1)

    # Method that will handle all the logic of a battle in Pokémom
    def core_gameplay():

        def display_options():
            if type(opponent) == Trainer:
                print(f"\n\tOpponent: {opponent.list_pokémon[0]}")
            elif type(opponent) == Pokémon: 
                print(f"\n\tOpponent: {opponent}")
            print(f"\tPlayer: {player.list_pokémon[0]}\n")
            option = input("What option do you want to do:\n" \
                "\t1: Attack\n" \
                "\t2: Use Object\n" \
                "\t3: Change Pokémon\n" \
                "\t4: Flee\n"
            )
            return option
        
        def attack():
            counter = 1
            if not player.list_pokémon[0].is_ko:
                if type(opponent) == Trainer:
                    deal_damage(player.list_pokémon[0], opponent.list_pokémon[0])
                    if opponent.list_pokémon[0].is_ko:
                        player.list_pokémon[0].gain_exp(enemy_level= opponent.list_pokémon[0].level)
                        while counter < len(player.list_pokémon):
                            sleep(1)
                            player.list_pokémon[counter].gain_exp(enemy_level= opponent.list_pokémon[0].level, primary= False)
                            counter += 1
                        sleep(1)
                elif type(opponent) == Pokémon:
                    deal_damage(player.list_pokémon[0],opponent)
                    if opponent.is_ko:
                        player.list_pokémon[0].gain_exp(enemy_level= opponent.level)
                        while counter < len(player.list_pokémon):
                            sleep(1)
                            player.list_pokémon[counter].gain_exp(enemy_level= opponent.level, primary= False)
                            counter += 1
                        sleep(2)
                return True
            else:
                clearscreen()
                print(f"Your {player.list_pokémon[0].name} is K.O, He's unable to fight!")
                return False
        
        def use_object():
            if type(opponent) == Trainer:
                if not player.use_item(in_battle_vs_trainer= True):
                    return False
                return None
            elif type(opponent) == Pokémon:
                if not player.use_item(in_battle_vs_wild_pok=True, wild_pokémon= opponent):
                    return False
                elif opponent.is_wild == False:
                    return True
                return None
        
        def flee():
            if type(opponent) == Trainer:
                clearscreen()
                print("You can't escape in a battle versus a trainer!")
                return False
            elif type(opponent) == Pokémon:
                if player.list_pokémon[0].is_ko:
                    clearscreen()
                    print("You can't escape with your pokémon KO, change your Pokémon!")
                    return False
                rng = random.randint(0,10)
                if rng <= 7:
                    print("You managed to escape!")
                    sleep(1)
                    return True
                else:
                    print("You failed to escape!")
                    sleep(1)
                    return None
        
        def opponent_response():
             # this code handle what happend after the player has done a turn in the battle
            if type(opponent) == Trainer:
                if opponent.list_pokémon[0].is_ko:
                    if check_is_ko(fighter= opponent):
                        clearscreen()
                        return True
                    else:
                        opponent.change_pokemon()
                        return False
                else:
                    deal_damage(opponent.list_pokémon[0], player.list_pokémon[0])
                    clearscreen()
                    if check_is_ko(fighter= player):
                        return True
            if type(opponent) == Pokémon:
                if not opponent.is_ko:
                    deal_damage(opponent, player.list_pokémon[0])
                    clearscreen()
                    if check_is_ko(fighter = player):
                        return True
                else:
                    clearscreen()
                    return True
        
        
        '''
        Entry point of core_gameplay method
        '''
        while True:
            result = False
            option = display_options() 
            match option:
                case '1'| 'Attack'| 'attack':
                    result = attack()
                    if result:
                        pass
                    else:
                        continue
                case '2'| 'use object'| 'Use Object':
                    result = use_object()
                    if result == None:
                        sleep(1)
                        pass
                    elif result:
                        break
                    else:
                        sleep(1)
                        clearscreen()
                        continue
                case '3'| 'Change Pokémon'| 'change'| 'change pokémon':
                    player.change_pokemon()
                case '4'| 'Flee'| 'flee':
                   result = flee()
                   if result == None:
                       pass
                   elif result:
                       clearscreen()
                       break
                   else:
                       continue
                case _:
                    clearscreen()
                    print('Invalid input! Try again')
                    continue
            
            result = opponent_response()
            if result:
                break
            else:
                pass    
            
        # this code is executed when when we are out of the loop and are in a battle vs a trainer (going out of the loop = win or loss)
        if type(opponent) == Trainer:
            if not check_is_ko(fighter= player) and check_is_ko(fighter= opponent):
                print(f"You have defeated {opponent.name}")
                money_gained = random.randint(1250,3600)
                print(f"You have won {money_gained} Poké-Dollars!")
                player.inventory.manage_money(money_gained)
                sleep(2)
            elif check_is_ko(fighter= player) and not check_is_ko(fighter= opponent):
                for pokémon in opponent.list_pokémon:
                    pokémon.health = pokémon.max_health
                print("You have lost the fight!")
                pre_lost = player.inventory.money
                money_lost = random.randint(-3600,-1250)
                player.inventory.manage_money(money_lost)
                print(f"You have lost {pre_lost - player.inventory.money} Poké-Dollars!")
                sleep(2)
        
        clearscreen()
    
    '''
    Entry Point of battle method

    '''
    if type(opponent) == Trainer and opponent.has_lost_vs_player:
        print(f"You have already won vs {opponent.name}")   
    else:
        if not check_is_ko(fighter= player):
            intro_battle()
            core_gameplay()
        else:
            print("You can't engage in battle when all your Pokémon are K.O!")
    
    