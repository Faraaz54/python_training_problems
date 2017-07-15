inp = int(raw_input())
l = [int(i) for i in raw_input().split()]
sum1, sum2, sum3 = 0, 0, 0
for i, v in enumerate(l, start=1):
    if i % 3 == 1:
        sum1 = sum1 + v
    elif i % 3 == 2:
        sum2 = sum2 + v
    elif i % 3 == 0:
        sum3 = sum3 + v

print sum1, sum2, sum3
