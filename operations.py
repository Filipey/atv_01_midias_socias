import json
from typing import Dict, List

from enums import TerminalColors
from models import BaseStats, Champion, ChampionSkill
from populate_dict import (
    add_assasin,
    add_fighter,
    add_mage,
    add_marksman,
    add_support,
    add_tank,
)


def populate_dict(dict: Dict[int, Champion]) -> None:
    add_marksman(0, dict)
    add_mage(1, dict)
    add_tank(2, dict)
    add_fighter(3, dict)
    add_assasin(4, dict)
    add_support(5, dict)
    print(
        TerminalColors.BLUE.value
        + "Dicionário populado com sucesso!"
        + TerminalColors.RESET.value
    )


def clear_dict(dict: Dict[int, Champion]) -> None:
    dict.clear()
    print(
        TerminalColors.GREEN.value
        + "\nO dicionário foi limpo com sucesso!"
        + TerminalColors.RESET.value
    )


def read_dict(dict: Dict[int, Champion]) -> None:
    print(
        TerminalColors.BLUE.value
        + "\nQuantidade de itens: "
        + TerminalColors.GREEN.value
        + f"{len(dict)}\n"
        + TerminalColors.RESET.value
    )

    if len(dict) == 0:
        print(
            TerminalColors.RED.value
            + "\nO dicionário não possui nenhum item!!"
            + TerminalColors.RESET.value
        )
        return

    for id, champion in dict.items():
        print(
            TerminalColors.YELLOW.value
            + f"{id}: "
            + TerminalColors.GREEN.value
            + f"{json.dumps(champion, indent=4)}"
            + TerminalColors.RESET.value
        )
        print()


def write_json(dict: Dict[int, Champion]) -> None:
    if len(dict) == 0:
        print(
            TerminalColors.RED.value
            + "\nO dicionário está vazio! O arquivo JSON não terá nenhum conteúdo!"
            + TerminalColors.RESET.value
        )
    with open("champions_dict.json", "w") as f:
        json.dump(dict, f, indent=4)
    print(
        TerminalColors.GREEN.value
        + "\nDicionário escrito no arquivo JSON com sucesso!"
        + TerminalColors.RESET.value
    )


def read_json() -> None:
    with open("champions_dict.json", "r") as f:
        champions = json.load(f)

        if len(champions) == 0:
            print(
                TerminalColors.RED.value
                + "\nO arquivo JSON não possui conteúdo!"
                + TerminalColors.RESET.value
            )
            return

        for id, champion in champions.items():
            print(
                TerminalColors.YELLOW.value
                + f"{id}: "
                + TerminalColors.GREEN.value
                + f"{json.dumps(champion, indent=4)}"
                + TerminalColors.RESET.value
            )
            print()


def write_tsv(dict: Dict[int, Champion]) -> None:
    with open("champions_dict_tsv.tsv", "w") as f:
        f.write(
            "id\tname\trole\tdamage_type\tpassive\tq_skill\tw_skill\te_skill\tr_skill"
            + "\thealth\thealth_regen\tmana\tmana_regen\trange\tattack_damage"
            + "\tattack_speed\tarmor\tmagic_resist\tmovement_speed\ttype\tprice\n"
        )

        if len(dict) == 0:
            print(
                TerminalColors.RED.value
                + "\nO dicionário está vazio! O arquivo TSV não terá nenhum conteúdo!!"
                + TerminalColors.RESET.value
            )
            return

        for id, champion_dict in dict.items():
            champion = Champion(**champion_dict)
            skills = [ChampionSkill(**skill_dict) for skill_dict in champion.skills]
            base_stats = BaseStats(**champion.base_stats)
            [passive_skill, q_skill, w_skill, e_skill, r_skill] = skills
            f.write(
                f"{id}\t{champion.name}\t{champion.role}\t{champion.damage_type}"
                + f"\t{passive_skill.to_tsv_string()}\t{q_skill.to_tsv_string()}\t{w_skill.to_tsv_string()}"
                + f"\t{e_skill.to_tsv_string()}\t{r_skill.to_tsv_string()}\t{base_stats.health}"
                + f"\t{base_stats.health_regen}\t{base_stats.mana}"
                + f"\t{base_stats.mana_regen}\t{base_stats.range}"
                + f"\t{base_stats.attack_damage}\t{base_stats.attack_speed}"
                + f"\t{base_stats.armor}\t{base_stats.magic_resist}"
                + f"\t{base_stats.movement_speed}\t{champion.type}\t{champion.price}\n"
            )

        print(
            TerminalColors.GREEN.value
            + "\nDicionário escrito no arquivo TSV com sucesso!"
            + TerminalColors.RESET.value
        )


def read_tsv() -> None:
    champions_count = 0
    with open("champions_dict_tsv.tsv") as f:
        for line in f:
            elements = line.strip().split("\t")
            if elements[0] != "id":
                [id, name, role, damage_type] = elements[0:4]
                skills = [skill for skill in elements[4:9]]
                base_stats_str = [stats for stats in elements[9:19]]
                [type, price] = elements[19:]

                skills_list = clear_tsv_skills_list(skills)
                stats = clear_tsv_base_status(base_stats_str)

                champion = Champion(
                    name, role, damage_type, skills_list, stats, type, price
                )
                print(
                    TerminalColors.YELLOW.value
                    + f"\n{id}: "
                    + TerminalColors.GREEN.value
                    + f"{champion}"
                    + TerminalColors.RESET.value
                )
                champions_count += 1
    if champions_count > 0:
        print(
            TerminalColors.BLUE.value
            + "\nO conteúdo do arquivo TSV foi impresso no formato JSON para facilitar a visualização!"
            + TerminalColors.RESET.value
        )
    else:
        print(
            TerminalColors.RED.value
            + "\nO arquivo TSV não possui conteúdo!"
            + TerminalColors.RESET.value
        )


def clear_tsv_skills_list(tsv_skills: List[str]):
    skills_list = []

    for skill in tsv_skills:
        [
            skill_name,
            mana_cost,
            skill_damage_type,
            skill_type,
        ] = skill.split(", ")
        skills_list.append(
            {
                "name": skill_name,
                "mana_cost": mana_cost,
                "damage_type": skill_damage_type,
                "type": skill_type,
            }
        )
    return skills_list


def clear_tsv_base_status(tsv_stats: List[str]):
    [
        health,
        h_r,
        mana,
        mana_r,
        range,
        a_d,
        a_s,
        armor,
        mr,
        m_s,
    ] = tsv_stats
    return {
        "health": health,
        "health_regen": h_r,
        "mana": mana,
        "mana_regen": mana_r,
        "range": range,
        "attack_damage": a_d,
        "attack_speed": a_s,
        "armor": armor,
        "magic_resist": mr,
        "moviment_speed": m_s,
    }
