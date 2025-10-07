N = int(input())
if N <= 1:
    print("NONE")
else:
    primes = []
    for num in range(2, N+1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    print(",".join(primes))
