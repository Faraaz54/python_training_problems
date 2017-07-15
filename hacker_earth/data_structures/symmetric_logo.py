for _ in xrange(int(raw_input())):
    N = int(raw_input())
    matrix = [[i for i in raw_input()] for j in range(N)]

    symmetric = True
    for i in range(N):
        if ''.join(matrix[i]) != ''.join(matrix[N-1-i]):
            symmetric = False
            break

    if symmetric:
        for i in range(N):
            if matrix[i] != list(reversed(matrix[i])):
                symmetric = False
                break

    if symmetric:
        print 'YES'
    else:
        print 'NO'



