# 怎样在两个字典中寻寻找相同点（比如相同的键、相同的值等等）？
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# keys
print('a.keys() & b.keys()')
print(a.keys() & b.keys())
print('a.keys() - b.keys()')
print(a.keys() - b.keys())

# items
print('a.items() & b.items()')
print(a.items() & b.items())

# 假如你想以现有字典构造一个排除几个指定键的新字典。 下面利用字典推导来实现这样的需求：排除a中的{'z', 'w'}
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)
