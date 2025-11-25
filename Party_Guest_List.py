
import sys


def main() -> None:
	data = sys.stdin.read().splitlines()
	if not data:
		print("Unique guests: 0")
		return

	# 第一行為 N，接下來 N 行為名字；保險起見處理可能的格式問題
	try:
		n = int(data[0].strip())
	except Exception:
		# 如果無法解析，則把所有列視為名字
		names = [line.strip() for line in data if line.strip()]
		unique = set(names)
		print(f"Unique guests: {len(unique)}")
		return

	names = []
	for i in range(1, 1 + n):
		if i < len(data):
			names.append(data[i].strip())
		else:
			# 如果實際行數比 N 少，跳出
			break

	unique = set(name for name in names if name != "")
	print(f"Unique guests: {len(unique)}")


if __name__ == "__main__":
	main()

