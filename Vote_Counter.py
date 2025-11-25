import sys


def main() -> None:
    data = sys.stdin.read().splitlines()
    if not data:
        return

    try:
        n = int(data[0].strip())
    except Exception:
        return

    votes = {}
    idx = 1
    for _ in range(n):
        if idx >= len(data):
            break
        name = data[idx].strip()
        idx += 1
        if name == "":
            continue
        votes[name] = votes.get(name, 0) + 1

    for name in sorted(votes.keys()):
        print(f"{name}: {votes[name]}")


if __name__ == "__main__":
    main()
