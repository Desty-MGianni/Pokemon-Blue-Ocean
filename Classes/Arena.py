from Classes.trainer import Trainer,Player
from Classes.battle import battle

class Arena:
    def __init__(self, name: str,sub_trainers: list, champion:Trainer, badge_name:str):
        self.name = name
        self.list_sub_trainers = sub_trainers
        self.champion = champion
        self.badge_name = badge_name
        self.won_badge = False
        self.pointer = 0
    
    def update_progression_arena(self):
        if self.list_sub_trainers[0].has_lost_vs_player:
            pointer += 1
            if self.list_sub_trainers[1].has_lost_vs_player:
                pointer += 1   

    def arena_loop(self, player: Player):
        while True:
            if not self.won_badge:
                if self.pointer == 0:
                    battle(player= player,opponent= self.list_sub_trainers[0])
                    self.update_progression_arena()
                    break
                elif self.pointer == 1:
                    battle(player= player, opponent= self.list_sub_trainers[1])
                    self.update_progression_arena()
                    break
                elif self.pointer == 2:
                    battle(player= player, opponent= self.champion)
                    if self.champion.has_lost_vs_player:
                        print(f"Congratulaton, you have earned your {self.badge_name}")
                        player.inventory.add_badge_and_no_duplicate(badge_name= self.badge_name)
                        self.won_badge = True
                    break
            else:
                print(f"You have already won the {self.badge_name}!")
                break
