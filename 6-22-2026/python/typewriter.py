import time
import argparse

parser = argparse.ArgumentParser("typewriter")
parser.add_argument(
    "text",
    default="Hello Typewriter Output World!"
)
parser.add_argument(
    "--delay", "-d",
    type=float,
    default=0.2,
    help="The amount of time, in seconds, between printing characters"
)

def typewriter(text: str, delay: float) -> None:
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)

def main() -> None:
    args = parser.parse_args()
    typewriter(text=args.text, delay=args.delay)

if __name__ == "__main__":
    main()
