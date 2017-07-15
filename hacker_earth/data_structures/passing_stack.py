for _ in xrange(int(raw_input())):
    pass_stack = []
    n_pass, init_id = map(int, raw_input().split())
    pass_stack.append(init_id)
    for i in xrange(n_pass):
        passes = raw_input().split()
        if passes[0] == 'P':
            pass_stack.append(passes[1])
        else:
            pass_stack.append(pass_stack[len(pass_stack)-2])


    print 'Player {0}'.format(pass_stack[len(pass_stack)-1])





