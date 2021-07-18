# 你想构建一个能支持迭代操作的自定义对象，并希望找到一个能实现迭代协议的简单方法。
# 实现一个以深度优先方式遍历树形节点的生成器


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)


if __name__ == '__main__':
    pass
