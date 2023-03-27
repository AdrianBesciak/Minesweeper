from enum import Enum


class GameState(Enum):
    NOT_STARTED = 1
    IN_PROGRESS = 2
    WON = 3
    FAILED = 4
    EXIT = 5
