from pathlib import Path
from pypdf import PdfReader
import typer

app = typer.Typer()

@app.command()
def main() -> None:
    print("Hello from CLI Typer!!!!!")
    # os.path.is
    path: Path = Path("./docs")
    # [print(x) for x in path.iterdir()]
    for p in path.iterdir():
        if p.is_file():
            if p.suffix.lower() == ".txt":
                print(f"{p} is a text file!")
                with p.open() as f:
                    print(f.readline())
            if p.suffix.lower() == ".pdf":
                print(f"{p} is a pdf file!")
                pdf_reader = PdfReader(p)
                pdf_meta = pdf_reader.metadata
                for m in pdf_meta.items():
                    print(m)
                page = pdf_reader.pages[0]
                print(page.extract_text())

    


if __name__ == "__main__":
    app()
