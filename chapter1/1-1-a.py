# 现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？

p = (4, 5)
data = ['ACME', 50, 91.1, (2012, 12, 21)]

print(p)
x, y = p
print(x)
print(y)
print(data)
name, shares, price, (year, month, day) = data
print(name)
print(shares)
print(price)
print(year)
print(month)
print(day)
