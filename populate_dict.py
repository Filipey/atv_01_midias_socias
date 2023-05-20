from typing import Dict

from enums import ChampionPrice, ChampionRole, ChampionType, DamageType, SkillType
from models import Champion


def add_marksman(key: int, dict: Dict[int, Champion]) -> None:
    dict[key] = {
        "name": "Ezreal",
        "role": ChampionRole.MARKSMAN.value,
        "damage_type": DamageType.BOTH.value,
        "skills": [
            {
                "name": "Rising Spell Force",
                "mana_cost": 0,
                "damage_type": DamageType.NONE.value,
                "type": SkillType.PASSIVE.value,
            },
            {
                "name": "Mystic Shot",
                "mana_cost": 28,
                "damage_type": DamageType.AD.value,
                "type": SkillType.ACTIVE.value,
            },
            {
                "name": "Essence Flux",
                "mana_cost": 50,
                "damage_type": DamageType.AP.value,
                "type": SkillType.ACTIVE.value,
            },
            {
                "name": "Arcane Shift",
                "mana_cost": 90,
                "damage_type": DamageType.AP.value,
                "type": SkillType.ACTIVE.value,
            },
            {
                "name": "Trueshot Barrage",
                "mana_cost": 100,
                "damage_type": DamageType.BOTH.value,
                "type": SkillType.ACTIVE.value,
            },
        ],
        "base_stats": {
            "health": 600,
            "health_regen": 4,
            "mana": 375,
            "mana_regen": 8.5,
            "range": 550,
            "attack_damage": 62,
            "attack_speed": 0.62,
            "armor": 24,
            "magic_resist": 30,
            "movement_speed": 325,
        },
        "type": ChampionType.RANGED.value,
        "price": ChampionPrice.HIGH_MEDIUM.value,
    }


def add_mage(key: int, dict: Dict[int, Champion]) -> None:
    dict[key] = {
        "name": "Syndra",
        "role": ChampionRole.MAGE.value,
        "damage_type": DamageType.AP.value,
        "skills": [
            {
                "name": "Transcendent",
                "mana_cost": 0,
                "damage_type": DamageType.NONE.value,
                "type": SkillType.PASSIVE.value,
            },
            {
                "name": "Dark Sphere",
                "mana_cost": 40,
                "damage_type": DamageType.AP.value,
                "type": SkillType.ACTIVE.value,
            },
            {
                "name": "Force of Will",
                "mana_cost": 60,
                "damage_type": DamageType.AP.value,
                "type": SkillType.ACTIVE.value,
            },
            {
                "name": "Scatter the Weak",
                "mana_cost": 50,
                "damage_type": DamageType.AP.value,
                "type": SkillType.ACTIVE.value,
            },
            {
                "name": "Unleashed Power",
                "mana_cost": 100,
                "damage_type": DamageType.AP.value,
                "type": SkillType.ACTIVE.value,
            },
        ],
        "base_stats": {
            "health": 563,
            "health_regen": 6.5,
            "mana": 480,
            "mana_regen": 8,
            "range": 550,
            "attack_damage": 54,
            "attack_speed": 0.62,
            "armor": 25,
            "magic_resist": 30,
            "movement_speed": 330,
        },
        "type": ChampionType.RANGED.value,
        "price": ChampionPrice.HIGH.value,
    }


def add_tank(key: int, dict: Dict[int, Champion]) -> None:
    dict[key] = {
        "name": "Poppy",
        "role": ChampionRole.TANK.value,
        "damage_type": DamageType.BOTH.value,
        "skills": [
            {
                "name": "Iron Ambassador",
                "mana_cost": 0,
                "damage_type": DamageType.AP.value,
                "type": SkillType.PASSIVE.value,
            },
            {
                "name": "Hammer Shock",
                "mana_cost": 35,
                "damage_type": DamageType.AD.value,
                "type": SkillType.ACTIVE.value,
            },
            {
                "name": "Steadfast Presence",
                "mana_cost": 50,
                "damage_type": DamageType.NONE.value,
                "type": SkillType.ACTIVE.value,
            },
            {
                "name": "Heroic Charge",
                "mana_cost": 70,
                "damage_type": DamageType.AD.value,
                "type": SkillType.ACTIVE.value,
            },
            {
                "name": "Keeper's Verdict",
                "mana_cost": 100,
                "damage_type": DamageType.AD.value,
                "type": SkillType.ACTIVE.value,
            },
        ],
        "base_stats": {
            "health": 610,
            "health_regen": 8,
            "mana": 280,
            "mana_regen": 7,
            "range": 125,
            "attack_damage": 64,
            "attack_speed": 0.62,
            "armor": 38,
            "magic_resist": 32,
            "movement_speed": 345,
        },
        "type": ChampionType.MELEE.value,
        "price": ChampionPrice.LOW.value,
    }


def add_fighter(key: int, dict: Dict[int, Champion]) -> None:
    dict[key] = {
        "name": "Xin Zhao",
        "role": ChampionRole.FIGHTER.value,
        "damage_type": DamageType.AD.value,
        "skills": [
            {
                "name": "Determination",
                "mana_cost": 0,
                "damage_type": DamageType.NONE.value,
                "type": SkillType.PASSIVE.value,
            },
            {
                "name": "Three Talon Strike",
                "mana_cost": 30,
                "damage_type": DamageType.AD.value,
                "type": SkillType.ACTIVE.value,
            },
            {
                "name": "Wind Becomes Lightning",
                "mana_cost": 60,
                "damage_type": DamageType.AD.value,
                "type": SkillType.ACTIVE.value,
            },
            {
                "name": "Audacious Charge",
                "mana_cost": 50,
                "damage_type": DamageType.AD.value,
                "type": SkillType.ACTIVE.value,
            },
            {
                "name": "Crescent Guard",
                "mana_cost": 100,
                "damage_type": DamageType.AD.value,
                "type": SkillType.ACTIVE.value,
            },
        ],
        "base_stats": {
            "health": 640,
            "health_regen": 8,
            "mana": 274,
            "mana_regen": 7.25,
            "range": 175,
            "attack_damage": 63,
            "attack_speed": 0.64,
            "armor": 35,
            "magic_resist": 32,
            "movement_speed": 345,
        },
        "type": ChampionType.MELEE.value,
        "price": ChampionPrice.LOW_MEDIUM.value,
    }


def add_assasin(key: int, dict: Dict[int, Champion]) -> None:
    dict[key] = {
        "name": "LeBlanc",
        "role": ChampionRole.ASSASSIN.value,
        "damage_type": DamageType.AP.value,
        "skills": [
            {
                "name": "Mirror Image",
                "mana_cost": 0,
                "damage_type": DamageType.NONE.value,
                "type": SkillType.PASSIVE.value,
            },
            {
                "name": "Sigil of Malice",
                "mana_cost": 50,
                "damage_type": DamageType.AP.value,
                "type": SkillType.ACTIVE.value,
            },
            {
                "name": "Distortion",
                "mana_cost": 60,
                "damage_type": DamageType.AP.value,
                "type": SkillType.ACTIVE.value,
            },
            {
                "name": "Etherial Chains",
                "mana_cost": 50,
                "damage_type": DamageType.AP.value,
                "type": SkillType.ACTIVE.value,
            },
            {
                "name": "Mimic",
                "mana_cost": 0,
                "damage_type": DamageType.NONE.value,
                "type": SkillType.ACTIVE.value,
            },
        ],
        "base_stats": {
            "health": 598,
            "health_regen": 7.5,
            "mana": 400,
            "mana_regen": 8,
            "range": 525,
            "attack_damage": 55,
            "attack_speed": 0.62,
            "armor": 22,
            "magic_resist": 30,
            "movement_speed": 340,
        },
        "type": ChampionType.RANGED.value,
        "price": ChampionPrice.MEDIUM.value,
    }


def add_support(key: int, dict: Dict[int, Champion]) -> None:
    dict[key] = {
        "name": "Millio",
        "role": ChampionRole.SUPPORT.value,
        "damage_type": DamageType.AP.value,
        "skills": [
            {
                "name": "Fired Up!",
                "mana_cost": 0,
                "damage_type": DamageType.AP.value,
                "type": SkillType.PASSIVE.value,
            },
            {
                "name": "Ultra Mega Fire Kick",
                "mana_cost": 50,
                "damage_type": DamageType.AP.value,
                "type": SkillType.ACTIVE.value,
            },
            {
                "name": "Cozy Campfire",
                "mana_cost": 90,
                "damage_type": DamageType.NONE.value,
                "type": SkillType.ACTIVE.value,
            },
            {
                "name": "Warm Hugs",
                "mana_cost": 50,
                "damage_type": DamageType.NONE.value,
                "type": SkillType.ACTIVE.value,
            },
            {
                "name": "Breath of Life",
                "mana_cost": 100,
                "damage_type": DamageType.NONE.value,
                "type": SkillType.ACTIVE.value,
            },
        ],
        "base_stats": {
            "health": 560,
            "health_regen": 5,
            "mana": 365,
            "mana_regen": 11.5,
            "range": 525,
            "attack_damage": 48,
            "attack_speed": 0.62,
            "armor": 28,
            "magic_resist": 30,
            "movement_speed": 330,
        },
        "type": ChampionType.RANGED.value,
        "price": ChampionPrice.HIGH.value,
    }
