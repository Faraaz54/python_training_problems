length = int(raw_input())

lst = sorted(map(int,  raw_input().split()))

print length

zipped = zip([i for i in range(2,51)], [j for j in range(1, 50)])

print len(zipped)
