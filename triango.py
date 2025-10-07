sides = list(map(int, input().split()))

a, b, c = sides

if a + b > c and a + c > b and b + c > a:
    print("Yes")
else:
    print("No")
