from rich.console import Console
from rich.panel import Panel

console = Console()

def bordered_panel(texto: str, isArquivo: bool) -> None:
    """Cria um painel com borda para o texto.
    
    Args:
        texto: String ou caminho do arquivo
        isArquivo: Indica se o texto é um caminho de arquivo
    """
    content = texto if not isArquivo else open(texto, 'r').read()
    panel = Panel(content, title="Texto", border_style="green")
    console.print(panel)

def expanded_panel(texto: str, isArquivo: bool) -> None:
    """Cria um painel expandido para o texto.
    
    Args:
        texto: String ou caminho do arquivo
        isArquivo: Indica se o texto é um caminho de arquivo
    """
    content = texto if not isArquivo else open(texto, 'r').read()
    panel = Panel(content, expand=True, title="Expandido", border_style="blue")
    console.print(panel)