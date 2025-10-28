def transform(line: str) -> str:
	vowels = set('aeiouAEIOU')
	out_chars = []
	for ch in line:
		if ch == ' ':
			out_chars.append(ch)
		elif ch.isalpha():
			if ch in vowels:
				out_chars.append(ch.upper())
			else:
				out_chars.append(ch.lower())
		else:
			out_chars.append(ch)
	return ''.join(out_chars)


def main() -> None:
	try:
		s = input()
	except EOFError:
		return
	print(transform(s))


if __name__ == '__main__':
	main()

