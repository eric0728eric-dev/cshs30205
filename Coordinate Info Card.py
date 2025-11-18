"""
Coordinate Info Card

讀取一列三個整數 x y z，將它們存成一個元組，並印出座標資訊卡。

輸入格式: 一行，包含三個以空格分隔的整數 x y z
輸出格式:
X: x值
Y: y值
Z: z值
"""

def main():
	try:
		# 讀一行，切割並轉成整數
		parts = input().strip().split()
		x, y, z = map(int, parts)
	except Exception:
		# 若輸入無效，使用 (0, 0, 0) 作為預設值
		x, y, z = 0, 0, 0

	coords = (x, y, z)  # 儲存為元組

	# 印出座標資訊卡
	print(f"X: {coords[0]}")
	print(f"Y: {coords[1]}")
	print(f"Z: {coords[2]}")


if __name__ == '__main__':
	main()
