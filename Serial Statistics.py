import sys


def compute_stats(nums):
	n = len(nums)
	total = sum(nums)
	mean = total / n if n > 0 else 0.0
	sorted_nums = sorted(nums)
	if n == 0:
		median = 0.0
	elif n % 2 == 1:
		median = float(sorted_nums[n // 2])
	else:
		median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2.0
	return total, mean, median


def main():
	line = sys.stdin.readline()
	if not line:
		return
	parts = line.strip().split()
	try:
		nums = [int(p) for p in parts if p != '']
	except ValueError:
		return

	if len(nums) == 0:
		print('Sum: 0, Mean: 0.00, Median: 0.00')
		return

	total, mean, median = compute_stats(nums)
	print(f"Sum: {total}, Mean: {mean:.2f}, Median: {median:.2f}")


if __name__ == '__main__':
	main()

