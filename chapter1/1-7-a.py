# 你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3

print(d)
for key in d:
    print(key, d[key])
