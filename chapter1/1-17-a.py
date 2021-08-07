# 从字典中提取子集
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# 获取prices中价格大于200的子集
p1 = {key: value for key, value in prices.items() if value > 20}
# 获取prices中名字在tech_names内的子集
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
