from Classes.arena import Arena
from Classes.shop import Shop
class City:
    def __init__(self, name: str, has_arena: bool, arena_info: list):
        self.name = name
        if has_arena:
            self.arena = Arena(arena_info[0],arena_info[1],arena_info[2],arena_info[3])
        
    pass