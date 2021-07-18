# 你想实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不一样。
# 生产某个范围内浮点数的生成器


def frange(start, stop, interval):
    x = start
    while x < stop:
        yield x
        x += interval


for i in frange(1, 2, 0.125):
    print(i)

# 一个函数中需要有一个 yield 语句即可将其转换为一个生成器。 跟普通函数不同的是，生成器只能用于迭代操作。
# 下面是一个实验，向你展示这样的函数底层工作机制
# 展示yield的工作原理


def countdown(n):
    print(f'开始从{n}减到0')
    while n > 0:
        yield n
        n -= 1
    print(f'结束')


c = countdown(3)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
