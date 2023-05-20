import json
from typing import List

from enums import ChampionPrice, ChampionRole, ChampionType, DamageType, SkillType


class ChampionSkill:
    name: str
    mana_cost: int
    damage_type: DamageType
    type: SkillType

    def __init__(self, name, mana_cost, damage_type, type) -> None:
        self.name = name
        self.mana_cost = mana_cost
        self.damage_type = damage_type
        self.type = type

    def __str__(self) -> str:
        return json.dumps(self.__dict__, indent=4)

    def to_tsv_string(self) -> str:
        return f"{self.name}, {self.mana_cost}, {self.damage_type}, {self.type}"


class BaseStats:
    health: int
    health_regen: float
    mana: int
    mana_regen: float
    range: int
    attack_damage: int
    attack_speed: float
    armor: int
    magic_resist: int
    movement_speed: int

    def __init__(
        self,
        health,
        health_regen,
        mana,
        mana_regen,
        range,
        attack_damage,
        attack_speed,
        armor,
        magic_resist,
        movement_speed,
    ) -> None:
        self.health = health
        self.health_regen = health_regen
        self.mana = mana
        self.mana_regen = mana_regen
        self.range = range
        self.attack_damage = attack_damage
        self.attack_speed = attack_speed
        self.armor = armor
        self.magic_resist = magic_resist
        self.movement_speed = movement_speed

    def __str__(self) -> str:
        return json.dumps(self.__dict__, indent=4)


class Champion:
    name: str
    role: ChampionRole
    damage_type: DamageType
    skills: List[ChampionSkill]
    base_stats: BaseStats
    type: ChampionType
    price: ChampionPrice

    def __init__(
        self, name, role, damage_type, skills, base_stats, type, price
    ) -> None:
        self.name = name
        self.role = role
        self.damage_type = damage_type
        self.skills = skills
        self.base_stats = base_stats
        self.type = type
        self.price = price

    def __str__(self) -> str:
        return json.dumps(self.__dict__, indent=4)
