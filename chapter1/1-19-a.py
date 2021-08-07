# 计算平方和
nums = [1, 2, 3, 4, 5]
print(sum(x * x for x in nums))

# 将元组作为csv输出
s = ('ACME', 50, 123.45)
print(','.join(str(a) for a in s))

# 找出shares最小的字典，和最小的值
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
print(min(p['shares'] for p in portfolio))
print(min(portfolio, key=lambda share: share['shares']))


