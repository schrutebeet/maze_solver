from enum import IntEnum, auto

class Role(IntEnum):
    # the 'auto' class will automatically enumerate the class variables [ENEMY = 1, ENTRANCE = 2, ...]
    NONE = 0
    ENEMY = auto()
    ENTRANCE = auto()
    EXIT = auto()
    EXTERIOR = auto()
    REWARD = auto()
    WALL = auto()
