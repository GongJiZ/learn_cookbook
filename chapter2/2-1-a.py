# 分隔字符串
import re
line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'[,;\s]\s*', line))
