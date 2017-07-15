from operator import itemgetter
sol = []
for _ in xrange(int(raw_input())):
    _length, _queries = map(int, raw_input().split())
    _counter = [0] * (_length + 1)
    st = [ord(i) for i in raw_input()]
    moves = []
    for i in xrange(_queries):
        l, r = map(int, raw_input().split())
        moves.append((l-1, r-1))

    for move in sorted(moves, key=itemgetter(0, 1)):
        l1, r1 = move
        for pos in range(l1, r1+1):
            _counter[pos] += 1

    sti = "".join(chr((x - v - 97) % 26 + 97) for x, v in zip(st, _counter))
    sol.append(sti)

for i in sol:
    print i


