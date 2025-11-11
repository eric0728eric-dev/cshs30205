import sys

line = sys.stdin.readline().strip()
if line == "":
    print(0)
else:
    hours = [float(x) for x in line.split()]
    total_hours = sum(hours)
    regular_hours = min(total_hours, 40.0)
    overtime_hours = max(total_hours - 40.0, 0.0)
    pay = regular_hours * 180.0 + overtime_hours * 270.0
    print(int(pay))