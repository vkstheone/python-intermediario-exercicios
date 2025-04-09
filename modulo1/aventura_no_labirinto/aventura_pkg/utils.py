"""Módulo com funções utilitárias para o jogo."""

from rich.console import Console
import time

console = Console()

def imprime_instrucoes():
    """Imprime as instruções do jogo formatadas."""
    console.print("[bold cyan]Instruções do Jogo:[/]", style="underline")
    console.print("Use as setas do teclado para mover o jogador (J).")
    console.print("Coletar itens (*) dá 10 pontos cada.")
    console.print("Chegue à saída (S) para vencer!")
    console.print("Pressione ESC para sair a qualquer momento.")

def animacao_vitoria(nome):
    """Animação recursiva para celebrar a vitória.

    Args:
        nome (str): Nome do jogador.
    """
    def animar(contador=3):
        if contador == 0:
            console.print(f"[bold green]Parabéns, {nome}! Você venceu![/]", style="blink")
            return
        console.clear()
        console.print(f"[yellow]Contagem regressiva: {contador}[/]", style="bold")
        time.sleep(1)
        animar(contador - 1)
    animar()