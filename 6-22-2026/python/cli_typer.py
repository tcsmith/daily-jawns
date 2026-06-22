from typing import Annotated
import typer

from typewriter import typewriter

app = typer.Typer(add_completion=False)
@app.command()
def main(
    text: Annotated[str, typer.Argument()] = "Hello from Typer CLI",
    delay: Annotated[float, typer.Option()] = 0.3
):
    typewriter(text=text, delay=delay)

if __name__ == "__main__":
    app()