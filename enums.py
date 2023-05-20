from enum import Enum


class MenuOptions(Enum):
    WRITE_JSON = 0
    WRITE_TSV = 1
    READ_JSON = 2
    READ_TSV = 3
    POPULATE_DICT = 4
    CLEAR_DICT = 5
    READ_DICT = 6
    EXIT = 7


class ChampionRole(Enum):
    MARKSMAN = "marksman"
    MAGE = "mage"
    TANK = "tank"
    FIGHTER = "fighter"
    ASSASSIN = "assasin"
    SUPPORT = "support"


class ChampionType(Enum):
    RANGED = "ranged"
    MELEE = "melee"


class DamageType(Enum):
    AP = "hability power"
    AD = "physical damage"
    BOTH = "hability power and physical damage"
    NONE = "none"


class SkillType(Enum):
    PASSIVE = "passive"
    ACTIVE = "active"


class ChampionPrice(Enum):
    HIGH = 6300
    HIGH_MEDIUM = 4800
    MEDIUM = 3150
    LOW_MEDIUM = 1350
    LOW = 450


class TerminalColors(Enum):
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RESET = "\033[0m"
