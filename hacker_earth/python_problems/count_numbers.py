import re

inp = int(raw_input())
if inp == 0:
    print 0
count_list = []
for _ in xrange(0, inp):
    l = int(raw_input())
    s = raw_input()
    num = [i for i in re.findall('\d+|\D+', s) if i.isdigit()]
    count_list.append(len(num))

for i in count_list:
    print i