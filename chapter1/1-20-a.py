# 现在假设你必须在两个字典中执行查找操作（比如先从 a 中找，如果找不到再在 b 中找）
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
d = {'x': 5, 'l': 6}

from collections import ChainMap

c = ChainMap(a, b, d)

print(c['x'])
print(c['y'])
print(c['z'])
print(c['l'])
print(list(c.keys()))
print(list(c.values()))
print(c)
