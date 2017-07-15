import timeit
import random

input_list = [random.randint(0, 100) for i in range(20)]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

print(timeit.timeit('''

import random

input_list = [random.randint(0, 1000) for i in range(200)]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = [i for i in input_list if div_by_five(i)]
for i in xyz:
    i
''', number = 5000))