# 在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a file
if __name__ == '__main__':
    f = ['1', '2', '22', '33', '44', '55', '66', '11', '22', '33', '55']
    for line, prevlines in search(f, '1', 5):
        for pline in prevlines:
            print(pline, end='')
        print(line, end='')
        print('-' * 20)
