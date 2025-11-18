"""
Warehouse Inventory Management

使用串列儲存庫存，每個項目為 (ID, Name, Stock) 的元組。
讀取 N 筆初始庫存；之後處理 M 個操作：
- UPDATE id delta：調整指定 ID 的庫存（可以為正或負數）
- QUERY id：查詢指定 ID 的庫存並輸出

注意：元組不可變，更新時需要建立新元組，並替換串列中的那一筆。
輸出格式：
ID: <id>, Name: <name>, Stock: <stock>
"""

def main():
	try:
		n = int(input().strip())
	except Exception:
		n = 0

	# 儲存庫存為串列，元素為 (id, name, stock)
	inventory = []
	for _ in range(n):
		try:
			parts = input().strip().split()
			item_id = parts[0]
			name = parts[1]
			stock = int(parts[2])
		except Exception:
			# 忽略格式錯誤的行
			continue
		inventory.append((item_id, name, stock))

	try:
		m = int(input().strip())
	except Exception:
		m = 0

	for _ in range(m):
		try:
			parts = input().strip().split()
			cmd = parts[0]
		except Exception:
			continue

		if cmd == 'UPDATE':
			# UPDATE id delta
			item_id = parts[1]
			delta = int(parts[2])

			# 找到索引，更新元組
			for i, item in enumerate(inventory):
				if item[0] == item_id:
					new_stock = item[2] + delta
					inventory[i] = (item[0], item[1], new_stock)
					break

		elif cmd == 'QUERY':
			# QUERY id
			item_id = parts[1]
			for item in inventory:
				if item[0] == item_id:
					print(f"ID: {item[0]}, Name: {item[1]}, Stock: {item[2]}")
					break


if __name__ == '__main__':
	main()

