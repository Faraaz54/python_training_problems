length = int(raw_input())
harry_bag = map(int, raw_input().split())
n, X = map(int, raw_input().split())
monk_bag = []
for i in range(n):
    inst = raw_input()
    if inst == 'Harry':
        monk_bag.append(harry_bag.pop(0))
    elif inst == 'Remove':
        monk_bag.pop()

    if sum(monk_bag) == X:
        print len(monk_bag)
        break
    elif len(harry_bag) == 0:
        print '-1'
        break



