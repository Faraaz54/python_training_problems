length, level = map(int, raw_input().split())
ques = [int(i) for i in raw_input().split()]
marks = 0
count = 0
for i in xrange(len(ques)):
    if ques[i] <= level:
        marks += 1
    elif ques[i] > level and count == 0:
        count += 1
        continue
    else:
        break

print marks

