import json
import datetime
j_file = open('city.list.json','r').read()
data = json.loads(j_file)
count = 0
for dct in data:
    for key in dct:
        if isinstance(dct[key],dict):
            for skey in dct[key]:
                print key,skey,dct[key][skey]
        else:
            print key,dct[key]
    count += 1
    if count == 10:
        break






