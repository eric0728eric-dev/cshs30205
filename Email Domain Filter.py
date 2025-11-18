
"""
Email Domain Filter

讀取一個合格網域字串（如 @gmail.com），接著讀取 N 筆電子郵件；
將所有以合格網域結尾的電子郵件收集到串列中並輸出該串列。

輸入格式：
第一行：合格網域（字串）
第二行：整數 N
接下來 N 行：每行一個電子郵件字串

輸出格式：
一行，印出符合條件的電子郵件串列 (Python list 格式)，若無則印出 []。
"""

def main():
	# 讀取合格網域
	try:
		domain = input().strip()
	except Exception:
		domain = ""

	try:
		n = int(input().strip())
	except Exception:
		n = 0

	qualified = []
	for _ in range(n):
		try:
			email = input().strip()
		except Exception:
			email = ""
		if domain and email.endswith(domain):
			qualified.append(email)

	print(qualified)


if __name__ == '__main__':
	main()

