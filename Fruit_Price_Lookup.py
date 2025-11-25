import sys


def main() -> None:
    data = sys.stdin.read().splitlines()
    if not data:
        return

    idx = 0
    try:
        n = int(data[idx].strip())
    except Exception:
        return
    idx += 1

    prices = {}
    for _ in range(n):
        if idx >= len(data):
            break
        line = data[idx].strip()
        idx += 1
        if not line:
            continue
        parts = line.split()
        # 假設水果名稱不含空白；第二個欄位為價格
        if len(parts) >= 2:
            name = parts[0]
            price = parts[1]
            prices[name] = price

    if idx >= len(data):
        return

    try:
        m = int(data[idx].strip())
    except Exception:
        return
    idx += 1

    for _ in range(m):
        if idx >= len(data):
            break
        q = data[idx].strip()
        idx += 1
        print(prices.get(q, ""))


if __name__ == "__main__":
    main()
