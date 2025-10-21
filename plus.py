def main():
    total = 0
    while True:
        try:
            s = input().strip()
        except EOFError:
            break
        if s == "":
            continue
        try:
            n = int(s)
        except ValueError:
            continue
        if n == 0:
            break
        total += n
    print(f"sum = {total}")

if __name__ == "__main__":
    main()
