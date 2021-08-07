# 分隔字符串
import re
line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'[,;\s]\s*', line))

# 分隔字符串且保留风格符号
print(re.split(r'(;|,|\s)\s*', line))
print(re.split(r'([;,\s]\s*)', ))
