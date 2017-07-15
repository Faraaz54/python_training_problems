file_open = open('code.txt', 'r')


def code_gen():
    for c1 in range(100):
        for c2 in range(100):
            for c3 in range(100):
                yield (c1, c2, c3)


for line in file_open.readlines():
    sequence = tuple([int(x) for x in line.split()])
    for (c1, c2, c3) in code_gen():
        if (c1, c2, c3) == sequence:
            print ('code found: {0}'.format((c1, c2, c3)))

    if not line:
        break















