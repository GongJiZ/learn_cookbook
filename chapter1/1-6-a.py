# 怎样实现一个键对应多个值的字典（也叫 multidict）？
from collections import defaultdict

d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['b'].append(1)
print(d)
