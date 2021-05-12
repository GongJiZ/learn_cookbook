# 你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
# 最简单的过滤序列元素的方法就是使用列表推导。取出所有整数或负数
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

# 节省内存的做法
pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)

# filter 输出所有数字
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False
print(list(filter(is_int, values)))

# compress
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
is_count = [n > 5 for n in counts]
from itertools import compress
print(list(compress(addresses, is_count)))
