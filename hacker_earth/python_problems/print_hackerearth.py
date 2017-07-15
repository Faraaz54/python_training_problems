'''l = ['h', 'c', 'k', 'r', 'a', 'e', 'h', 't', 'r', 'a', 'e']
l.sort()
print l'''

count_h = 0
count_a = 0
count_c = 0
count_k = 0
count_e = 0
count_r = 0
count_t = 0

inp = int(raw_input())
for i in raw_input():
    if i == 'h':
        count_h += 1
    elif i == 'a':
        count_a += 1
    elif i == 'c':
        count_c += 1
    elif i == 'k':
        count_k += 1
    elif i == 'e':
        count_e += 1
    elif i == 'r':
        count_r += 1
    elif i == 't':
        count_t += 1

main_count = count_h/2
if count_a/2 < main_count:
    main_count = count_a/2
if count_c < main_count:
    main_count = count_c
if count_k < main_count:
    main_count = count_k
if count_e/2 < main_count:
    main_count = count_e/2
if count_r/2 < main_count:
    main_count = count_r/2
if count_t < count_h/2:
    main_count = count_t

print main_count


