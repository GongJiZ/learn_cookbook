# 你想遍历一个可迭代对象中的所有元素，但是却不想使用for循环。
items = [1, 2, 3, 4]
it = iter(items)

while True:
    try:
        print(next(it))
    except StopIteration:
        print('没有了')
        break

it = iter(items)
while True:
    i = next(it, None)
    if not i:
        print('没有了')
        break
    print(i)
