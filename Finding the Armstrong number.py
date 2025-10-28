import sys


def is_armstrong(x: int) -> bool:
	s = str(x)
	n = len(s)
	total = sum(int(ch) ** n for ch in s)
	return total == x


def main() -> None:
	line = sys.stdin.readline()
	if not line:
		return
	parts = line.strip().split()
	if len(parts) < 2:
		return
	try:
		A = int(parts[0])
		B = int(parts[1])
	except ValueError:
		return

	results = []
	for i in range(A, B + 1):
		if is_armstrong(i):
			results.append(str(i))

	if results:
		print(' '.join(results))


if __name__ == '__main__':
	main()

