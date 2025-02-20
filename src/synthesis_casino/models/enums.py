from enum import Enum

class SettingChipsType(Enum):
    SUM = 1
    SUB = 2
    SET = 0

class RouletteType(Enum):
    COLOR = 1
    EVEN_ODD = 2
    
class RouletteColor(Enum):
    RED = 1
    BLACK = 2
    GREEN = 3

class RouletteEvenOdd(Enum):
    EVEN = 1
    ODD = 2