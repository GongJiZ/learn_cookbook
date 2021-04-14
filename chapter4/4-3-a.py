# 你想实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不一样。


def frange(start, stop, interval):
    x = start
    while x < stop:
        yield x
        x += interval


for i in frange(1, 2, 0.125):
    print(i)
