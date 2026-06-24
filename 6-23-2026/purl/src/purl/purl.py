from typing import Annotated
import http.client

import typer

app = typer.Typer()

@app.command()
def main(host: Annotated[str, typer.Argument()]) -> None:
    conn = http.client.HTTPSConnection(host)
    conn.request(method="GET", url="/")
    response = conn.getresponse()
    print(response.status, response.reason)
    print(response.readline())

