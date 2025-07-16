import random
import os
from time import sleep
from Classes.trainer import Trainer,Player
from Classes.pokemon import Pokémon

# method that handle the battling mechanic with the emblematic 4 choices
def battle(player:Player, opponent: Trainer | Pokémon):
    # universal nested method that is use by player and opponent for dealing damages.
    
    def clearscreen(numlines= 100):
        """Clear the console.
        numlines is an optional argument used only as a fall-back.
        """
        # Thanks to Steven D'Aprano, http://www.velocityreviews.com/forums
        if os.name == "posix":
            # Unix, Linux, macOS, BSD, etc.
            os.system('clear')
        elif os.name in ("nt", "dos", "ce"):
            # DOS/Windows
            os.system('CLS')
        else:
            # Fallback for other operating systems.
            print('\n' * numlines)

    def attack(pokemon_attacking: Pokémon, pokemon_receiving: Pokémon):
        damages = pokemon_attacking.pok_damages()
        print(f"{pokemon_attacking.name} launch an attack!")
        sleep(1)
        print(f"{pokemon_attacking.name} has inflicted {damages} to {pokemon_receiving.name}!")
        pokemon_receiving.lose_health(damages)
        sleep(1)

    # Nested method that verify if object inpout is Knocked Out (ONly available for object containing pokémons)
    def check_is_ko(fighter: Pokémon | Trainer):
        if type(fighter) == Pokémon:
            return fighter.is_ko
        elif isinstance(fighter, (Trainer,Player)):
            return fighter.check_all_pok_ko()
    
    def intro_battle():
        intro_message = "You have entered in a battle versus "
        if type(opponent) == Trainer:
            intro_message += f"{opponent.name}"
            print(intro_message)
            print(f"{opponent.name} choose {opponent.list_pokémon[0].name}!")
        elif type(opponent) == Pokémon:
            intro_message += f"a wild {opponent.name}"
            print(intro_message)
        print(f"{player.list_pokémon[0].name}, Go!")

    def core_gameplay():
        while True:
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
            
            match option:
                case '1'| 'Attack'| 'attack':
                    if not player.list_pokémon[0].is_ko:
                        if type(opponent) == Trainer:
                            attack(player.list_pokémon[0], opponent.list_pokémon[0])
                            if opponent.list_pokémon[0].is_ko:
                                player.list_pokémon[0].gain_exp(opponent.list_pokémon[0].level)
                                sleep(1)
                        elif type(opponent) == Pokémon:
                            attack(player.list_pokémon[0],opponent)
                            if opponent.is_ko:
                                player.list_pokémon[0].gain_exp(opponent.level)
                                sleep(1)
                    else:
                        print(f"Your {player.list_pokémon[0].name} is K.O, He's unable to fight!")
                        continue
                case '2'| 'use object'| 'Use Object':
                    if type(opponent) == Trainer:
                        if not player.use_item(in_battle_vs_trainer= True):
                            continue
                    elif type(opponent) == Pokémon:
                        if not player.use_item(in_battle_vs_wild_pok=True,wild_pokémon= opponent):
                            continue
                        elif opponent.is_wild == False:
                            break
                case '3'| 'Change Pokémon'| 'change'| 'change pokémon':
                    player.change_pokemon()
                case '4'| 'Flee'| 'flee':
                    if type(opponent) == Trainer:
                        print("You can't escape in a battle versus a trainer!")
                        continue
                    elif type(opponent) == Pokémon:
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
            
            # this code handle what happend after the player has done a turn in the battle
            if type(opponent) == Trainer:
                if opponent.list_pokémon[0].is_ko:
                    if check_is_ko(fighter= opponent):
                        break
                    else:
                        opponent.change_pokemon()
                else:
                    attack(opponent.list_pokémon[0], player.list_pokémon[0])
                    if check_is_ko(fighter= player):
                        break
            if type(opponent) == Pokémon:
                if not opponent.is_ko:
                    attack(opponent, player.list_pokémon[0])
                    if check_is_ko(fighter = player):
                        break
                else:
                    break
            clearscreen()

        if type(opponent) == Trainer:
            if not check_is_ko(fighter= player) and check_is_ko(fighter= opponent):
                print(f"You have defeated {opponent.name}")
                money_gained = random.randint(1250,3600)
                print(f"You have won {money_gained} Poké-Dollars!")
                player.inventory.manage_money(money_gained)
            elif check_is_ko(fighter= player) and not check_is_ko(fighter= opponent):
                print("You have lost the fight!")
                pre_lost = player.inventory.money
                money_lost = random.randint(-3600,-1250)
                player.inventory.manage_money(money_lost)
                print(f"You have lost {pre_lost - player.inventory.money} Poké-Dollars!")
        
        sleep(2)
        clearscreen()
    '''

    Entry Point of the method
    
    '''   
    if not check_is_ko(fighter= player):
        intro_battle()
        core_gameplay()
    else:
        print("You can't engage in battle when all your Pokémon are K.O!")
    
    