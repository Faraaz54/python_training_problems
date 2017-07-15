from collections import Counter
import re


cnt = Counter(re.findall('.',raw_input()))
print cnt
m = max(cnt.values())
res = [ord(i) for i in cnt.keys() if cnt[i] == m]
print chr(min(res)), cnt[chr(min(res))]


