from collections import Counter
for _ in xrange(int(raw_input())):
    s = raw_input()
    t = s.replace('SUVOJIT','a')
    cnt = Counter(t.replace('SUVO', 'b'))
    print 'SUVO = {0}, SUVOJIT = {1}'.format(cnt['b'], cnt['a'])






