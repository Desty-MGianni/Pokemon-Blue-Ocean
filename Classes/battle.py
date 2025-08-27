import random
import beaupy
from time import sleep
from Classes.clearscreen import clearscreen
from Classes.trainer import Trainer,Player
from Classes.pokemon import Pokémon

# method that handle the battling mechanic with the emblematic 4 choices
def battle(player:Player, opponent: Trainer | Pokémon):

    # universal method that is use by player and opponent for dealing damages.
    def __deal_damage(pokemon_attacking: Pokémon, pokemon_attacked: Pokémon) -> None:
        damages: int = pokemon_attacking.pok_damages()
        print(f"{pokemon_attacking.name} launch an attack!")
        sleep(1)
        print(f"{pokemon_attacking.name} has inflicted {damages} to {pokemon_attacked.name}!")
        pokemon_attacked.lose_health(damages)
        sleep(1)

    # Method that verify if the parameter is Knocked Out (Only available for object containing pokémons)
    def __check_is_ko(fighter: Pokémon | Trainer) -> bool:
        if type(fighter) == Pokémon:
            return fighter.is_ko
        elif isinstance(fighter, (Trainer)):
            return fighter.check_all_pok_ko()
    
    # Method that is called in the beginning of a battle.
    def __intro_battle() -> None:
        sleep(1.5)
        clearscreen()
        intro_message: str = "You have entered in a battle versus "
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
    
    # return an int that is the index of the choice makde in the list we input.
    def __display_options() -> str:
        if type(opponent) == Trainer:
            print(f"\n\tOpponent: {opponent.list_pokémon[0]}")
        elif type(opponent) == Pokémon: 
            print(f"\n\tOpponent: {opponent}")
        print(f"\tPlayer: {player.list_pokémon[0]}\n")
        choice = beaupy.select(
            options= ["Attack", "Use Object", "Change Pokémon", "Flee"],
            return_index= False,
            cursor= "--->"
        )
        return choice
    
    def __gain_xp() -> None:
        import math
        base: int = random.randint(1,2)
        counter: int = 1
        full: int = 0
        if type(opponent) == Trainer:
            full = math.floor(base * (opponent.list_pokémon[0].level **2) + base * player.list_pokémon[0].level / 4)
        elif type(opponent) == Pokémon:
            full = math.floor(base * (opponent.level**2) + base * player.list_pokémon[0].level/4)
        player.list_pokémon[0].gain_exp(full)
        sleep(1)
        full = math.ceil(full / 2)
        while counter < len(player.list_pokémon):
            player.list_pokémon[counter].gain_exp(full)
            counter += 1
            sleep(1)
    
    # Method that will handle all the logic of a battle in Pokémom
    def __core_gameplay() -> None:
        
        def attack() -> bool:
            counter: int = 1
            if not player.list_pokémon[0].is_ko:
                if type(opponent) == Trainer:
                    __deal_damage(player.list_pokémon[0], opponent.list_pokémon[0])
                    if opponent.list_pokémon[0].is_ko:
                        __gain_xp()
                        sleep(1)
                elif type(opponent) == Pokémon:
                    __deal_damage(player.list_pokémon[0],opponent)
                    if opponent.is_ko:
                        __gain_xp()
                return True
            else:
                clearscreen()
                print(f"Your {player.list_pokémon[0].name} is K.O, He's unable to fight!")
                return False
        
        def use_object() -> bool | None:
            if type(opponent) == Trainer:
                if not player.use_item(in_battle_vs_trainer= True):
                    return False
                return None
            elif type(opponent) == Pokémon:
                if not player.use_item(in_battle_vs_wild_pok=True, wild_pokémon= opponent):
                    return False
                elif not opponent.is_wild:
                    return True
                return None
        
        def flee() -> bool | None:
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
                    if __check_is_ko(fighter= opponent):
                        clearscreen()
                        return True
                    else:
                        opponent.change_pokemon()
                        return False
                else:
                    __deal_damage(opponent.list_pokémon[0], player.list_pokémon[0])
                    clearscreen()
                    if __check_is_ko(fighter= player):
                        return True
            if type(opponent) == Pokémon:
                if not opponent.is_ko:
                    __deal_damage(opponent, player.list_pokémon[0])
                    clearscreen()
                    if __check_is_ko(fighter = player):
                        return True
                else:
                    clearscreen()
                    return True
          
        '''
        Entry point of core_gameplay method
            break = end of battle
            pass = action done, looping normaly
            continue = canceled action, the player can still play.
        '''
        while True:
            result: bool = False
            option: int = __display_options() 
            match option:
                case "Attack":
                    result = attack()
                    if result:
                        pass
                    else:
                        continue
                case "Use Object":
                    result = use_object()
                    if result is None:
                        sleep(1)
                        pass
                    elif result:
                        break
                    else:
                        sleep(1)
                        clearscreen()
                        continue
                case "Change Pokémon":
                    if player.change_pokemon():
                        pass
                    else:
                        continue
                case "Flee":
                   result = flee()
                   if result is None:
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
            if not __check_is_ko(fighter= player) and __check_is_ko(fighter= opponent):
                print(f"You have defeated {opponent.name}")
                money_gained: int = random.randint(1250,3600)
                print(f"You have won {money_gained} Poké-Dollars!")
                player.inventory.manage_money(money_gained)
                sleep(2)
            elif __check_is_ko(fighter= player) and not __check_is_ko(fighter= opponent):
                for pokémon in opponent.list_pokémon:
                    pokémon.health = pokémon.max_health
                print("You have lost the fight!")
                pre_lost: int = player.inventory.money
                money_lost: int = random.randint(-3600,-1250)
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
        if not __check_is_ko(fighter= player):
            __intro_battle()
            __core_gameplay()
        else:
            print("You can't engage in battle when all your Pokémon are K.O!")
    
    