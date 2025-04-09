"""Script principal para executar o jogo Aventura no Labirinto."""

import argparse
from rich.console import Console
from aventura_pkg import criar_labirinto, imprimir_labirinto, iniciar_jogador, mover, resolver_labirinto, imprime_instrucoes, animacao_vitoria
import time

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Jogo Aventura no Labirinto")
    parser.add_argument("--name", default="Aventureiro", help="Nome do jogador")
    parser.add_argument("--color", default="cyan", help="Cor principal do jogo (cyan, yellow, green)")
    parser.add_argument("--dificuldade", type=int, choices=[1, 2, 3], default=1, help="Dificuldade: 1 (fácil), 2 (médio), 3 (difícil)")
    parser.add_argument("--auto", action="store_true", help="Resolve o labirinto automaticamente")
    args = parser.parse_args()

    console.print(f"[bold {args.color}]Bem-vindo, {args.name}, ao Aventura no Labirinto![/]", style="underline")

    while True:
        console.clear()  # Limpa a tela antes de mostrar o menu
        console.print("\n[bold]Menu:[/]")
        console.print("1 - Jogar")
        console.print("2 - Instruções")
        console.print("3 - Resolver Automaticamente" if args.auto else "3 - Sair")
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                labirinto = criar_labirinto(args.dificuldade)
                pos, pontuacao = iniciar_jogador(labirinto)
                while True:
                    imprimir_labirinto(labirinto, pos)
                    console.print(f"Pontuação: {pontuacao}")
                    pos, pontuacao = mover(labirinto, pos, pontuacao)
                    if labirinto[pos[0]][pos[1]] == "S":
                        animacao_vitoria(args.name)
                        break
            case "2":
                imprime_instrucoes()
            case "3" if args.auto:
                labirinto = criar_labirinto(args.dificuldade)
                pos, _ = iniciar_jogador(labirinto)
                caminho = resolver_labirinto(labirinto, pos)
                if caminho:
                    for passo in caminho:
                        imprimir_labirinto(labirinto, passo)
                        time.sleep(0.5)
                    console.print("[bold green]Labirinto resolvido![/]")
                else:
                    console.print("[bold red]Sem solução![/]")
                break
            case "3":
                console.print(f"[bold {args.color}]Até logo, {args.name}![/]")
                break
            case _:
                console.print("[red]Opção inválida![/]")

if __name__ == "__main__":
    main()