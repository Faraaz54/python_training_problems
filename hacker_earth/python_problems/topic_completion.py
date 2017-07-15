class MyList(object):
    def __init__(self, students):
        self.students_list = students
        self.start = 0
        self.current = 0
        self.end = len(self.students_list)

    def __str__(self):
        return ' '.join(str(i) for i in self.students_list)

    def __len__(self):
        return len(self.students_list)

    def __iter__(self):
        return self

    def next(self):
        if self.current >= self.end:
            self.current = self.start
            a = self.students_list[self.current]
            self.current += 1
            return a
        else:
            b = self.students_list[self.current]
            self.current += 1
            return b

for _ in xrange(int(raw_input())):
    topics = int(raw_input())
    RI = map(int,raw_input().split())
    schedule = MyList(RI)
    day = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
    count = -1
    for i in schedule:
        if i==1:
            topics -= i
        count += 1
        if topics == 0:
            print day[count%7]
            break

'''T=int(input())
D=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
for i in range(0,T):
    a=int(input())
    c=map(int,raw_input().split())
    d=a%sum(c)
    f=0
    i=0
    if d!=0:
        while f<d:
            f=f+c[i]
            i+=1
        print D[i-1]
    else:
        for i in range(0,len(c)):
            if c[i]!=0:
                f=i
        print D[f]'''





