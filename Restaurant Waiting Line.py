"""
Restaurant Waiting Line

模擬餐廳候位系統，支援三種指令：
WAIT name -> 將名為 name 的顧客加入隊尾
CALL       -> 呼叫隊首顧客（先進先出），並印出 Call: {name}
EXIT       -> 結束程式輸入

若在 CALL 時隊伍為空，請印出 No one in line。
"""

def main():
	queue = []
	while True:
		try:
			line = input().strip()
		except EOFError:
			break
		except Exception:
			# 任何輸入錯誤視同結束
			break

		if not line:
			continue

		parts = line.split(maxsplit=1)
		cmd = parts[0]

		if cmd == 'EXIT':
			break
		elif cmd == 'WAIT':
			# 若有姓名，加入隊尾；如果沒有提供姓名，忽略
			if len(parts) > 1:
				name = parts[1]
				queue.append(name)
		elif cmd == 'CALL':
			if queue:
				name = queue.pop(0)
				print(f"Call: {name}")
			else:
				print("No one in line")
		else:
			# 未知指令：忽略
			continue


if __name__ == '__main__':
	main()

