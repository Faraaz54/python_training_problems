from collections import Counter
for _ in xrange(int(raw_input())):
    st = raw_input()
    cnt = Counter(st)

    if any([True for i in cnt.values() if i >= 2]):
        print 'Yes'
    else:
        print 'No'


