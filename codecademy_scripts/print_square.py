def print_square():
    for x in range(0,11):
        if x in (0,5,10):
            print '+' , ' -' * 4 , ' +' , ' -' * 4 , '+'
        else:
            print '|' , '  ' * 4 , ' |' , '  ' * 4 , '|'
print_square()
