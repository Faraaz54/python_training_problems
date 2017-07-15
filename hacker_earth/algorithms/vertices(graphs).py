for __ in xrange(int(raw_input())):
    lst = []
    for _ in xrange(int(raw_input())):

        x,y = map(int, raw_input().split())
        lst.append(x)
        lst.append(y)

    print len(set(lst))
