def sumall(*args):
    sum = 0
    for i in range(0, len(args)):
        sum += args[i]

    return sum

print sumall(1,2,5,66)
