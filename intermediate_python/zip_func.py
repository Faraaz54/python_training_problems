import random

list_1 = [random.randint(0,100) for i in range(10)]
list_2 = [random.randint(0,100) for j in range(10)]
list_3 = [random.randint(0,100) for k in range(10)]

#for i,j in zip(list_1, list_2):
    #print i,j

xyz = list(zip(list_1, list_2))

print xyz
