from rich.console import Console
from rich.layout import Layout

console = Console()

def split_layout(texto: str, isArquivo: bool) -> None:
    """Divide a tela em duas partes verticais com o texto.
    
    Args:
        texto: String ou caminho do arquivo
        isArquivo: Indica se o texto é um caminho de arquivo
    """
    content = texto if not isArquivo else open(texto, 'r').read()
    layout = Layout()
    layout.split_column(
        Layout(name="upper"),
        Layout(name="lower")
    )
    layout["upper"].update(content)
    layout["lower"].update(content[::-1])  # Texto invertido
    console.print(layout)

def row_layout(texto: str, isArquivo: bool) -> None:
    """Divide a tela em duas partes horizontais com o texto.
    
    Args:
        texto: String ou caminho do arquivo
        isArquivo: Indica se o texto é um caminho de arquivo
    """
    content = texto if not isArquivo else open(texto, 'r').read()
    layout = Layout()
    layout.split_row(
        Layout(name="left"),
        Layout(name="right")
    )
    layout["left"].update(content)
    layout["right"].update(f"Length: {len(content)}")
    console.print(layout)