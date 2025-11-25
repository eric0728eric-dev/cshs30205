import sys


def main() -> None:
    data = sys.stdin.read().splitlines()
    if not data:
        print([])
        return

    try:
        n = int(data[0].strip())
    except Exception:
        n = 0

    arrived = set()
    idx = 1
    for _ in range(n):
        if idx >= len(data):
            break
        line = data[idx].strip()
        idx += 1
        if line == "":
            continue
        try:
            seat = int(line)
        except Exception:
            continue
        arrived.add(seat)

    all_seats = set(range(1, 11))
    missing = sorted(all_seats - arrived)
    print(missing)


if __name__ == "__main__":
    main()
