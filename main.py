import pathlib


def load_joke():
    text = pathlib.Path(__file__).with_name("entry.txt").read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("entry.txt is empty — nothing to deliver")
    return text


def main():
    print(load_joke())


if __name__ == "__main__":
    main()
