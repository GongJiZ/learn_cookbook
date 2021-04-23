# 怎样从一个集合中获得最大或者最小的 N 个元素列表？
from heapq import nlargest, nsmallest

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(nlargest(3, nums))
print(nsmallest(3, nums))

# 通过价格比较取最大的两个和最小的两个
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(nlargest(2, portfolio, key=lambda s: s['price']))
print(nsmallest(2, portfolio, key=lambda s: s['price']))
