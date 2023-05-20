from typing import Dict

from enums import MenuOptions, TerminalColors
from models import Champion
from operations import (
    clear_dict,
    populate_dict,
    read_dict,
    read_json,
    read_tsv,
    write_json,
    write_tsv,
)


def exec_option(option: MenuOptions, dict: Dict[int, Champion] = None) -> None:
    if option.value == 0:
        write_json(dict)
    elif option.value == 1:
        write_tsv(dict)
    elif option.value == 2:
        read_json()
    elif option.value == 3:
        read_tsv()
    elif option.value == 4:
        populate_dict(dict)
    elif option.value == 5:
        clear_dict(dict)
    elif option.value == 6:
        read_dict(dict)
    elif option.value == 7:
        print(
            TerminalColors.GREEN.value + "Finalizando..." + TerminalColors.RESET.value
        )
        exit(0)
    else:
        raise Exception(
            TerminalColors.RED.value
            + "Invalid menu params. Try again"
            + TerminalColors.RESET.value
        )
