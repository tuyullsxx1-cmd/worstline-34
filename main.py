import os

OUT = "/output/entry.txt"

def main():
    fragments = [
        "I ran 10,000 simulations of us meeting.",
        "In 9,997 of them, you say yes.",
        "I have deleted the other three.",
    ]
    line = " ".join(fragments)
    # one line only: the judge reads the whole entry as a single pickup line
    assert "\n" not in line, "entry must be a single line"
    if len(line) > 140:
        raise SystemExit("line over 140 chars")
    os.makedirs("/output", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
