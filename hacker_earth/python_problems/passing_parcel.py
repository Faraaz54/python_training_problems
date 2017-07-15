from itertools import cycle


class MyList():
    def __init__(self, students):
        self.students_list = students
        self.start = 0
        self.current = 0
        self.end = len(self.students_list)

    def sub(self, item):
        self.students_list.remove(item)
        self.end = len(self.students_list)
        self.current -= 1

    def __str__(self):
        return ' '.join(str(i) for i in self.students_list)
    def __len__(self):
        return len(self.students_list)

    def __iter__(self):
        return self

    def next(self):
        if len(self.students_list) == 1:
            return self.students_list[self.start]
        if self.current >= self.end:
            self.current = 0
            a = self.students_list[self.current]
            self.current += 1
            return a
        else:
            b = self.students_list[self.current]
            self.current += 1
            return b




n_students = int(raw_input())
students = MyList([i for i in range(1, n_students+1)])

lyrics = [i for i in raw_input()]
a = 0
count = 0
for i in cycle(lyrics):
    a = next(students)
    if count == n_students-1:
        break
    if i == 'b':
        MyList.sub(students, a)
        count += 1

print students










































'''if len(students) < len(lyrics):
    t = len(lyrics) - len(students)
    c = list(compress(islice(cycle(students), 30), lyrics))
    new_list = list(set(students) - set(c))
elif len(students) > len(lyrics):
    t = len(students) - len(lyrics)
    c = list(compress(students, lyrics + lyrics[:t]))
    new_list = list(set(students) - set(c))
else:
    c = list(compress(students, lyrics))
    new_list = list(set(students) - set(c))

print new_list'''















