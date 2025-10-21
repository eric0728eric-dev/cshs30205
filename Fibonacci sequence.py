def compute(num):
    a, b = 0, 1
    out = []
    for _ in range(num):
        out.append(str(a))
        a, b = b, a + b
    print(" ".join(out) + " ")

if __name__ == "__main__":
    num = int(input().strip())
    compute(num)