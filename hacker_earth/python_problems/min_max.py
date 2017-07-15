import re

n = int(raw_input())
s = map(lambda x: int(x), raw_input().split())
#l = [int(i) for i in re.findall('(\d+)', s)]
s.sort()
max_n = max(s)
min_n = min(s)
val = "YES"
#print s
while min_n < max_n:
    if min_n not in s:
        val = "NO"
        break
    min_n += 1
print(val)




