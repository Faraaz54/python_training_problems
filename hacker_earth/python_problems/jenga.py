import itertools
from collections import defaultdict
height = int(raw_input())
chance = int(raw_input())
max = height
check_level = 0
out = -1
tower = defaultdict(int)
for i in range(chance):
    level, block = raw_input().split()
    if block == 'M':
        tower[int(level)] += 10
    else:
        tower[int(level)] += 1

    if tower[int(level)] > 10 and int(level) == int(check_level):
        max -= 1
    elif tower[int(level)] > 10 and level != max:
        out = i+1
        break

    elif level == max and tower[int(level)] == 12:
        max -= 1
    check_level = level
print '\n{0}'.format(out)
























'''fall = ['LM', 'ML', 'RM', 'MR']
out = -1
for i in range(chance):
    level, block = raw_input().split()
    moves[int(level)-1] += block
    for k in range(len(moves)-1):
        if any(match in moves[k] for match in fall) and moves[k+1] != '':
            out = i

print out'''









