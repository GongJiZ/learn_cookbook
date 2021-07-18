

# 反方向迭代一个序列
a = [1, 2, 3, 4]


# 通过在自定义类上实现 __reversed__() 方法来实现反向迭代，数字递增输出
class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1


if __name__ == '__main__':
    pass
