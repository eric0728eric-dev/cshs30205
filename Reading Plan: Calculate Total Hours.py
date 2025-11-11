import sys

line = sys.stdin.readline().strip()
if line == "":
    print("0.0")
else:
    parts = line.split()
    total = sum(float(x) for x in parts)
    print(total)