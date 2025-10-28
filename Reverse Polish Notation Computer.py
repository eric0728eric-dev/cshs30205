import sys


def evaluate_rpn(line: str) -> int:
	tokens = line.strip().split()
	stack = []
	for tok in tokens:
		if tok in ('+', '-', '*') and len(tok) == 1:
			b = stack.pop()
			a = stack.pop()
			if tok == '+':
				stack.append(a + b)
			elif tok == '-':
				stack.append(a - b)
			else:  # '*'
				stack.append(a * b)
		else:
			stack.append(int(tok))

	return stack[-1]


def main():
	line = sys.stdin.readline()
	if not line:
		return
	result = evaluate_rpn(line)
	print(result)


if __name__ == '__main__':
	main()

