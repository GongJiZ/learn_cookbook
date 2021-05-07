# 如果你的程序包含了大量无法直视的硬编码切片，并且你想清理一下代码。
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost)
SHARES = slice(20, 23)
NUMS = slice(31, 37)
print(int(record[SHARES]) * float(record[NUMS]))
