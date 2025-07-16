from Classes.trainer import Trainer


class Arena:
    def __init__(self, name: str,sub_trainers: list, champion:Trainer, badge_name:str):
        self.name = name
        self.list_sub_trainers = sub_trainers
        self.champion = champion
        self.badge_name = badge_name
        print("Je suis le plus fort!")

