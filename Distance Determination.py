import math
s = input().strip()
parts = s.split()
if len(parts) >= 2:
    x, y = map(float, parts[:2])
else:
    x = float(parts[0]) if parts else float(input().strip())
    y = float(input().strip())
dist = math.hypot(x - 5, y - 6)
if dist <= 15:
    print("Inside")
else:
    print("Outside")