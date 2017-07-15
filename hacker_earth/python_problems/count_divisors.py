inp = raw_input().split()

l, r, k = int(inp[0]), int(inp[1]), int(inp[2])
count = 0

for i in range(l, r+1):
    if i % k == 0:
        count += 1

print count
