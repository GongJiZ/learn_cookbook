# 怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）？
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# zip
print(max(zip(prices.values(), prices.keys())))
print(min(zip(prices.values(), prices.keys())))
# sorted
print(sorted(zip(prices.values(), prices.keys())))
# values
print(max(prices.values()))
# lambda
print(prices[max(prices, key=lambda k: prices[k])])
print(max(prices, key=lambda k: prices[k]))
