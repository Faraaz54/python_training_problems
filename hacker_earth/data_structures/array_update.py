for _ in range(int(raw_input())):
    _length, K = map(int, raw_input().split())
    arr = [int(i) for i in raw_input().split()]
    if min(arr) < K:
        print K - min(arr)
    else:
        print '0'

