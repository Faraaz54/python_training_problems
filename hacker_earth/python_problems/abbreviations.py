f = []
for _ in xrange(int(raw_input())):
    f.append(raw_input())
inp_length = int(raw_input())
s = raw_input().split()
a = []

for i in range(len(s)):
    if s[i] not in f:
        a.append(s[i][0].upper())

print '.'.join(i for i in a)



