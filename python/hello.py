import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--name",
    default="Todd"
)
args = parser.parse_args()


def greeting_fn(name: str):
    return lambda name: print(f"Hi there {name} 👋")

def test_enumerate():
    pass

def do_map_things() -> None:
    myjawns = {"baz": "qux"}
    myjawns["foo"] = "bar"
    print(myjawns)

    for k,v in myjawns.items():
        print(f"{k}={v}")

    for index, (k, v) in enumerate(myjawns.items()):
        print(f"index={index}, {k}={v}")
        
def do_string_things() -> None:
    name = "Todd"
    print(name.capitalize())
    print(name.upper())
    print(len(name))
    print(name[:])
    print(name[1:])
    print(name.replace("d", "x"))
    print(name.find("o"))
    print(name.find("x"))
    print(", ".join(["Todd", "Erin", "Noodles", "Nutmeg"]))



def do_list_things() -> None:
    l = [1, 4, 7, 4, 7, 9, 3]
    print(l)
    l.sort(reverse=True)
    print(l)
    l.sort()
    print(l)
    l2 = l.copy()
    l2.sort(reverse=True)
    print(l)
    print(l2)

def do_a_bool_thing() -> str | None:
    # return "tood" or None
    return "" or None



def main() -> None:
    print("Hello Valve!")
    # name: str = input("What is your name? ")
    name = args.name
    print(f"Hello {name}")
    greet = greeting_fn(name=name)
    greet(name)

    l = [1, 2, 3, 4]
    doubled = [x * 2 for x in l]
    print(l)
    print(doubled)

    for tups in enumerate(l):
        print(tups)

    do_map_things()
    do_string_things()
    do_list_things()

    if do_a_bool_thing():
        print("its true")
    else:
        print("its false")

    d = {"foo": "bar"}
    if "foo" in d:
        print("foo is in d")

if __name__ == "__main__":
    main()
