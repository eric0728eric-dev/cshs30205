import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); c = int(next(it))
    min_unit = None
    for _ in range(n):
        a = int(next(it)); b = int(next(it))
        unit = b // a
        if min_unit is None or unit < min_unit:
            min_unit = unit
    if not min_unit or min_unit <= 0:
        print(0)
    else:
        print(c // min_unit)

if __name__ == "__main__":
    main()