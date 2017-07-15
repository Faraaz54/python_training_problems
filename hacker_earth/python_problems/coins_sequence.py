k = int(raw_input())
st = raw_input()
count = 0

for i in range((len(st)+1)-k):
    if len(set(st[i:i+k])) == len(st[i:i+k]):
        count +=1
        j=i+k
        while j < len(st):
            if len(set(st[i:j+1])) == k:
                count += 1
                j += 1

            else:
                break

print count
