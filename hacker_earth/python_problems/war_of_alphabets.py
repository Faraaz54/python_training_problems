from collections import Counter
for _ in xrange(int(raw_input())):
    alice = Counter(''.join(raw_input().split()))
    bob = Counter(''.join(raw_input().split()))
    a = Counter(alice-bob)
    b = Counter(bob-alice)
    if sum(a.values()) != 0 and sum(b.values()) != 0:
        print 'You draw some.'
    elif sum(a.values()) == 0:
        print 'You lose some.'
    elif sum(b.values()) == 0:
        print 'You win some.'






