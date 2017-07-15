import bisect
class queue():
    def __init__(self):
        self.q = []
        self.front = len(self.q)
        self.end = 0


    def __len__(self):
        return len(self.q)

    def __str__(self):
        return ' '.join(str(i) for i in self.q)

    def push(self, student):
        pos = -1
        if queue.isempty(self):
            self.q.append(student)
        elif student[0] not in set([i[0] for i in self.q]):
            self.q.insert(self.end , student)

        else:
            for i in range(0, len(self.q)/2):
                if self.q[i][0] == student[0]:
                    pos = i
                    self.q.insert(pos, student)
                    break

            if pos == -1:
                for i in range(len(self.q)/2, len(self.q)):
                    if self.q[i][0] == student[0]:
                        self.q.insert(i, student)
                        break


    def pop(self):
        return self.q.pop()

    def isempty(self):
        if len(self.q) == 0:
            return True
        return False


operations = int(raw_input())
student_q = queue()
for _ in xrange(operations):
    op = raw_input().split()
    if op[0] == 'E':
        school = int(op[1])
        num = int(op[2])
        student_q.push((school, num))
    else:
        out = student_q.pop()
        print '{0[0]} {0[1]}'.format(out)















