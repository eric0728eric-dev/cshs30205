import sys

line = sys.stdin.readline().strip()
if line == "":
    print(0)
else:
    nums = [int(x) for x in line.split()]
    avg = int(sum(nums) / len(nums)) 
    print(avg)
