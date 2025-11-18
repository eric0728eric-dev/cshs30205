
"""
Student Scoreboard

讀取 N 位學生的姓名與分數，將每位學生資料儲存為 (分數, 姓名) 的元組，
將整個串列依分數由高到低排序；若分數相同，則依姓名由 Z 到 A 排序。
最後印出依排序後的學生姓名，每行一個。
"""

def main():
	try:
		n = int(input().strip())
	except Exception:
		n = 0

	students = []
	for _ in range(n):
		try:
			parts = input().strip().split()
			name = parts[0]
			score = int(parts[1])
		except Exception:
			# 如果輸入不完整或格式錯誤，跳過該行
			continue
		students.append((score, name))

	# 直接使用 reverse=True，因為我們儲存 (score, name)，希望分數高在前，姓名 Z-A
	students.sort(reverse=True)

	for score, name in students:
		print(name)


if __name__ == '__main__':
	main()

