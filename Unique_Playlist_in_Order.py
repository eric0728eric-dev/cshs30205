import sys


def main() -> None:
    data = sys.stdin.read().splitlines()
    if not data:
        print([])
        return

    # 解析第一行為 N，否則把所有列視為歌曲
    try:
        n = int(data[0].strip())
        lines = data[1:1 + n]
    except Exception:
        lines = data

    seen = set()
    result = []
    for line in lines:
        name = line.strip()
        if name == "":
            continue
        if name not in seen:
            seen.add(name)
            result.append(name)

    print(result)


if __name__ == "__main__":
    main()
