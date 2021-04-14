# 如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。 那么怎样才能从这个可迭代对象中解压出 N 个元素出来？

# Python 的星号表达式可以用来解决这个问题。比如，你在学习一门课程，在学期末的时候， 你想统计下家庭作业的平均成绩，但是排除掉第一个和最后一个分数。
# 如果只有四个分数，你可能就直接去简单的手动赋值， 但如果有 24 个呢？
grades = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(grades)
first, *middle, last = grades
print(first)
print(middle)
print(last)
print(sum(middle)/len(middle))

# 另外一种情况，假设你现在有一些用户的记录列表，每条记录包含一个名字、邮件，接着就是不确定数量的电话号码。
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
print(record)
name, email, *phones = record
print(name)
print(email)
print(phones)


# 用for循环打印records
def do_foo(x, y):
    print(x)
    print(y)


def do_bar(z):
    print(z)


records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]
for name, *record in records:
    if name == 'foo':
        do_foo(*record)
    if name == 'bar':
        do_bar(*record)

# 用:号分割获取第一个和最后两个
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
print(line)
head, *body, left_foot, right_foot = line.split(':')
print(head)
print(body)
print(left_foot)
print(right_foot)
