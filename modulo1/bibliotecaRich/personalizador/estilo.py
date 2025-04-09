from rich.console import Console
from rich.text import Text

console = Console()

def colored_text(texto: str, isArquivo: bool) -> None:
    """Exibe o texto com cores diferentes.
    
    Args:
        texto: String ou caminho do arquivo
        isArquivo: Indica se o texto é um caminho de arquivo
    """
    content = texto if not isArquivo else open(texto, 'r').read()
    text = Text(content)
    text.stylize("bold magenta")
    console.print(text)

def highlighted_text(texto: str, isArquivo: bool) -> None:
    """Exibe o texto com destaque.
    
    Args:
        texto: String ou caminho do arquivo
        isArquivo: Indica se o texto é um caminho de arquivo
    """
    content = texto if not isArquivo else open(texto, 'r').read()
    text = Text(content)
    text.stylize("on yellow")
    console.print(text)