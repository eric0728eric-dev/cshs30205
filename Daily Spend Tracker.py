"""
Daily Spend Tracker

讀取 N (天數) 並讀取 N 行的每日花費（整數），
將花費存成串列，計算總花費與平均花費並輸出。

輸出格式: Total: T, Average: A
其中 T 為總花費（整數），A 為平均花費（小數點後 2 位）
"""

def main():
	try:
		n = int(input().strip())
	except Exception:
		# 若讀入失敗（例如輸入為空），視為 0 天
		n = 0

	spends = []
	for _ in range(n):
		# 將每一天的花費視為整數
		try:
			value = int(input().strip())
		except Exception:
			# 若讀取時有雜訊，視為 0
			value = 0
		spends.append(value)

	total = sum(spends)
	average = (total / n) if n > 0 else 0.0

	# 確保平均是兩位小數
	print(f"Total: {total}, Average: {average:.2f}")


if __name__ == "__main__":
	main()

