from typing import Dict

from enums import MenuOptions, TerminalColors
from menu import exec_option
from models import Champion


def main():
    print(
        TerminalColors.RED.value
        + "\nEste é um menu para interação do usuário. Para entender melhor o contexto da aplicação, leia o arquivo 'funcionamento.txt'!"
        + TerminalColors.RESET.value
    )
    data: Dict[int, Champion] = {}

    while True:
        option = input(
            TerminalColors.GREEN.value
            + "\nSelecione uma opção: "
            + TerminalColors.YELLOW.value
            + "\n0 \u2192 Escrever JSON"
            + "\n1 \u2192 Escrever TSV"
            + "\n2 \u2192 Ler JSON"
            + "\n3 \u2192 Ler TSV"
            + "\n4 \u2192 Popular Dicionário"
            + "\n5 \u2192 Limpar Dicionário"
            + "\n6 \u2192 Ler Dicionário"
            + "\n7 \u2192 Finalizar\n"
            + TerminalColors.RESET.value
        )

        if option in [str(option.value) for option in MenuOptions]:
            selected_option = MenuOptions(int(option))
            exec_option(selected_option, data)
        else:
            print(
                TerminalColors.RED.value
                + f"\nO valor '{option}' não é válido como uma opção."
                + TerminalColors.RESET.value
            )


if __name__ == "__main__":
    main()
