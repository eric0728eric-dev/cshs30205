# 計算矩形對角線長度
import math
length, width = map(int, input().split())
diagonal = math.sqrt(length ** 2 + width ** 2)
print(f"{diagonal:.2f}")
