# 你想使用 Unix Shell 中常用的通配符(比如 *.py , Dat[0-9]*.csv 等)去匹配文本字符串
# 找出ST结尾的字符串
# 找出10开头的字符串
# fnmatchcase区分大小写
from fnmatch import fnmatch, fnmatchcase

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
    '10A02 N BROADWAY',
]
for address in addresses:
    if fnmatch(address, '*ST'):
        print(address)
    if fnmatch(address, '10[0-9][0-9]*'):
        print(address)
