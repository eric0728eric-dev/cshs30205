import sys
import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.isqrt(n))
    i = 3
    while i <= r:
        if n % i == 0:
            return False
        i += 2
    return True

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    try:
        n = int(data[0])
    except ValueError:
        return
    print("YES" if is_prime(n) else "NO")

if __name__ == "__main__":
    main()