from Classes.trainer import Trainer,Player
from Classes.battle import battle

class Arena:
    def __init__(self, name: str, sub_trainers: list, champion: Trainer, badge_name: str):
        self.name: str = name
        self.list_sub_trainers: list[Trainer] = sub_trainers
        self.champion: Trainer = champion
        self.badge_name: str = badge_name
        self.won_badge: bool = False
        self.pointer: int = 0
    
    def update_progression_arena(self) -> None:
        if self.list_sub_trainers[self.pointer].has_lost_vs_player:
             self.pointer += 1

    def arena_loop(self, player: Player) -> None:
        while True:
            if self.won_badge:
                print(f"You have already won the {self.badge_name}!")
                break
            elif not self.won_badge and self.pointer < len(self.list_sub_trainers):
                battle(player= player,opponent= self.list_sub_trainers[self.pointer])
                self.update_progression_arena()
            else:
                battle(player= player, opponent= self.champion)
                if self.champion.has_lost_vs_player:
                    print(f"Congratulaton, you have earned your {self.badge_name}")
                    player.inventory.add_badge_and_no_duplicate(badge_name= self.badge_name)
                    self.won_badge = True
                    break
