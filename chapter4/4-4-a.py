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

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for n in self:
            yield from n.depth_first()


if __name__ == '__main__':
    root = Node(0)
    c1 = Node(1)
    c2 = Node(2)
    c3 = Node(3)
    c4 = Node(4)
    c5 = Node(5)
    c6 = Node(6)
    root.add_child(c1)
    c1.add_child(c2)
    c1.add_child(c3)
    c2.add_child(c4)
    c2.add_child(c5)
    c3.add_child(c6)
    for ch in root.depth_first():
        print(ch)
