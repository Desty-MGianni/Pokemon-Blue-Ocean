from Classes import trainer
from Classes.trainer import Trainer


class Arena:
    def __init__(self, sub_trainers: list, champion:Trainer, badge_name:str):
        self.list_sub_trainers = sub_trainers
        self.champion = champion
        self.badge_name = badge_name