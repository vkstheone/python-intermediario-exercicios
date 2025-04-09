from rich.console import Console
from rich.progress import Progress
import time

console = Console()

def simple_progress(texto: str, isArquivo: bool) -> None:
    """Mostra uma barra de progresso simples antes de exibir o texto.
    
    Args:
        texto: String ou caminho do arquivo
        isArquivo: Indica se o texto é um caminho de arquivo
    """
    content = texto if not isArquivo else open(texto, 'r').read()
    with Progress() as progress:
        task = progress.add_task("Processando...", total=100)
        for _ in range(100):
            progress.update(task, advance=1)
            time.sleep(0.02)
    console.print(content)

def spinning_progress(texto: str, isArquivo: bool) -> None:
    """Mostra um spinner antes de exibir o texto.
    
    Args:
        texto: String ou caminho do arquivo
        isArquivo: Indica se o texto é um caminho de arquivo
    """
    content = texto if not isArquivo else open(texto, 'r').read()
    with Progress() as progress:
        task = progress.add_task("Carregando...", total=None)
        for _ in range(50):
            progress.update(task)
            time.sleep(0.05)
    console.print(content)