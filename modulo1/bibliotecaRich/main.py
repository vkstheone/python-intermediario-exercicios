import argparse
from personalizador import (
    split_layout, row_layout,
    bordered_panel, expanded_panel,
    simple_progress, spinning_progress,
    colored_text, highlighted_text
)

MODULES = {
    "layout": {"split": split_layout, "row": row_layout},
    "painel": {"bordered": bordered_panel, "expanded": expanded_panel},
    "progresso": {"simple": simple_progress, "spinning": spinning_progress},
    "estilo": {"colored": colored_text, "highlighted": highlighted_text}
}

def main():
    parser = argparse.ArgumentParser(description="Formatador de texto com Rich")
    parser.add_argument("texto", help="Texto ou caminho do arquivo a ser formatado")
    parser.add_argument("-a", "--arquivo", action="store_true", 
                       help="Indica que o texto é um caminho de arquivo")
    parser.add_argument("-m", "--modulo", 
                       help="Módulo a ser usado (layout[0], painel[1], progresso[2], estilo[3])",
                       default="layout")
    parser.add_argument("-f", "--funcao",
                       help="Função a ser usada (depende do módulo escolhido)",
                       default="0")

    args = parser.parse_args()

    # Converter índices numéricos para nomes
    module_names = list(MODULES.keys())
    try:
        module_idx = int(args.modulo)
        module_name = module_names[module_idx]
    except ValueError:
        module_name = args.modulo

    if module_name not in MODULES:
        print(f"Módulo inválido. Opções: {', '.join(module_names)}")
        return

    module = MODULES[module_name]
    func_names = list(module.keys())
    try:
        func_idx = int(args.funcao)
        func_name = func_names[func_idx]
    except ValueError:
        func_name = args.funcao

    if func_name not in module:
        print(f"Função inválida para {module_name}. Opções: {', '.join(func_names)}")
        return

    func = module[func_name]
    func(args.texto, args.arquivo)

if __name__ == "__main__":
    main()