# 定义一个生成器函数，但是它会调用某个你想暴露给用户使用的外部状态值
# 你想让你的生成器暴露外部状态给用户， 别忘了你可以简单的将它实现为一个类，然后把生成器函数放到 __iter__() 方法中
from collections import deque


class Linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


if __name__ == '__main__':
    lines = Linehistory(['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee'])
    for line in lines:
        if 'dddd' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')
