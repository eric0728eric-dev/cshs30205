def is_strong(password: str) -> bool:
	if len(password) < 8:
		return False
	has_upper = any(ch.isupper() for ch in password)
	has_lower = any(ch.islower() for ch in password)
	has_digit = any(ch.isdigit() for ch in password)
	return has_upper and has_lower and has_digit


def main() -> None:
	try:
		pwd = input()
	except EOFError:
		return
	print('Strong' if is_strong(pwd) else 'Weak')


if __name__ == '__main__':
	main()

