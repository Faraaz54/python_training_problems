list1 = [1, 5, 2, 65, 85, 10]


def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False
#list comprehension--builds and loads the list in memory--takes up memory

xyz = [i for i in list1 if div_by_five(i)]
print xyz
#generator -- generates a sequence on the fly but does not commit to memory--slower
xyz = (i for i in list1 if div_by_five(i))
print xyz

for i in xyz:
    print i





