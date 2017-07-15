import re
s = raw_input()
w = re.findall('\s',s)
print len(w)