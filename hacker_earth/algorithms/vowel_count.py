for _ in xrange(int(raw_input())):
    s = raw_input().lower()
    count = 0
    for i in s:
        if i in ['a','e','i','o','u']:
            count += 1

    print count
