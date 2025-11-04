# ...existing code...
import sys

def find_max(nums):
    if not nums:
        return None
    m = nums[0]
    for x in nums[1:]:
        if x > m:
            m = x
    return m

def find_min(nums):
    if not nums:
        return None
    m = nums[0]
    for x in nums[1:]:
        if x < m:
            m = x
    return m

def main():
    line = sys.stdin.read().strip()
    if not line:
        return
    nums = list(map(int, line.split()))
    print(f"最大值: {find_max(nums)}")
    print(f"最小值: {find_min(nums)}")

if __name__ == "__main__":
    main()
# ...existing code...