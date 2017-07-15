from collections import Counter
_length = int(raw_input())
arr = Counter([int(i) for i in raw_input().split()])
for _ in range(int(raw_input())):
    number = int(raw_input())
    c = arr[number]
    if c != 0:
        print c
    else:
        print 'NOT PRESENT'

