"""Módulo para criação e exibição do labirinto."""

import os
from rich.console import Console

console = Console()

def criar_labirinto(dificuldade=1):
    """Cria um labirinto com base na dificuldade escolhida.

    Args:
        dificuldade (int): Nível de dificuldade (1 = fácil, 2 = médio, 3 = difícil).

    Returns:
        list: Matriz representando o labirinto com paredes (#), caminho ( ), itens (*) e saída (S).
    """
    if dificuldade == 1:
        return [
            ["#", "#", "#", "#", "#"],
            ["#", " ", " ", "*", "#"],
            ["#", " ", "#", " ", "#"],
            ["#", "*", " ", " ", "S"],
            ["#", "#", "#", "#", "#"]
        ]
    elif dificuldade == 2:
        return [
            ["#", "#", "#", "#", "#", "#"],
            ["#", " ", " ", "*", " ", "#"],
            ["#", "#", " ", "#", " ", "#"],
            ["#", " ", "*", " ", "#", "#"],
            ["#", " ", " ", " ", " ", "S"],
            ["#", "#", "#", "#", "#", "#"]
        ]
    else:  # dificuldade 3
        return [
            ["#", "#", "#", "#", "#", "#", "#"],
            ["#", " ", " ", "*", " ", " ", "#"],
            ["#", "#", " ", "#", "#", " ", "#"],
            ["#", " ", "*", " ", " ", "*", "#"],
            ["#", "#", " ", "#", " ", " ", "S"],
            ["#", " ", " ", " ", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#"]
        ]

def imprimir_labirinto(labirinto, pos_jogador):
    """Imprime o labirinto no terminal com o jogador na posição atual.

    Args:
        labirinto (list): Matriz do labirinto.
        pos_jogador (tuple): Posição (linha, coluna) do jogador.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal (Windows ou Linux/Mac)
    console.print("\n")  # Adiciona uma linha em branco no topo
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
            if (i, j) == pos_jogador:
                console.print("[bold green]J[/]", end=" ")
            else:
                if labirinto[i][j] == "#":
                    console.print("[grey]#[/]", end=" ")
                elif labirinto[i][j] == "*":
                    console.print("[yellow]*[/]", end=" ")
                elif labirinto[i][j] == "S":
                    console.print("[red]S[/]", end=" ")
                else:
                    console.print(" ", end=" ")
        console.print()  # Nova linha após cada linha do labirinto