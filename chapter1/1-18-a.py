# 你有一段通过下标访问列表或者元组中元素的代码，但是这样有时候会使得你的代码难以阅读， 于是你想通过名称来访问元素。
stock = {'name': 'abc', 'price': 12, 'num': 5}

from collections import namedtuple

stock1 = namedtuple('stock1', ['name', 'price', 'num'])
s1 = stock1('abc', 12, 5)
print(s1.price * s1.num)

# 元组中的值能够替换
s1 = s1._replace(price=100)
print(s1.price * s1.num)
