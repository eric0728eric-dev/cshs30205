# ...existing code...
import sys

line = sys.stdin.readline().strip()
if line == "":
    print(0)
else:
    p = int(line)
    if p >= 100:
        p -= 10
    print(p)
