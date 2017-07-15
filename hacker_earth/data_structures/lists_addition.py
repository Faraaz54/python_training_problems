from itertools import starmap
l = int(raw_input())
RI = lambda : map(int, raw_input().split())

lst1 = RI()
lst2 = RI()

print ' '.join(map(str ,list(starmap(lambda x,y:x+y, [i for i in zip(lst1, lst2)]))))




