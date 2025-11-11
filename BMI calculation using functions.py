import sys

def calculate_bmi(height_cm, weight_kg):
    height_m = float(height_cm) / 100.0
    return float(weight_kg) / (height_m * height_m)

line = sys.stdin.readline().strip()
if line == "":
    print(0.0)
else:
    h_str, w_str = line.split()
    bmi = calculate_bmi(h_str, w_str)
    print(bmi)