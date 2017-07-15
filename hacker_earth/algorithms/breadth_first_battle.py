from collections import deque


def corner(point, loc):
    r = point[0]
    c = point[1]
    global points
    lst = []
    if loc == 0:
        l = [(0,1),(1,1),(1,0)]
        for i in l:
            if points[i] == 1:
                lst.append(i)
    elif loc == 1:
        l = [(0,c-1),(1, c-1),(1, c)]
        for i in l:
            if points[i] == 1:
                lst.append(i)
    elif loc == 2:
        l = [(r-1,0),(r-1,c+1),(r,c+1)]
        for i in l:
            if points[i] == 1:
                lst.append(i)
    elif loc == 3:
        l = [(r-1,c),(r-1,c-1),(r,c-1)]
        for i in l:
            if points[i] == 1:
                lst.append(i)
    return lst


def edge(point ,ed):
    lst = []
    global points
    r = point[0]
    c = point[1]
    if ed == 0:
        e = [(r,c-1),(r,c+1),(r+1,c-1),(r+1,c+1),(r+1,c)]
        for i in e:
            if points[i] == 1:
                lst.append(i)
    elif ed == 1:
        e = [(r, c - 1), (r, c + 1), (r - 1, c - 1), (r - 1, c + 1), (r - 1, c)]
        for i in e:
            if points[i] == 1:
                lst.append(i)
    elif ed == 2:
        e = [(r-1, c), (r+1, c), (r - 1, c + 1), (r + 1, c + 1), (r, c+1)]
        for i in e:
            if points[i] == 1:
                lst.append(i)
    elif ed == 3:
        e = [(r - 1, c), (r + 1, c), (r - 1, c - 1), (r + 1, c - 1), (r, c - 1)]
        for i in e:
            if points[i] == 1:
                lst.append(i)
    return lst


def middle(point):
    lst = []
    r = point[0]
    c = point[1]
    m = [(r-1, c),(r+1, c),(r,c+1),(r,c-1),(r-1,c-1),(r-1,c+1),(r+1,c-1),(r+1,c+1)]
    for i in m:
        if points[i] == 1:
            lst.append(i)
    return lst



def position(r,c, point):
    index = 0
    corners = [(0, 0), (0, c), (r, 0), (r, c)]
    if point in corners:
        return corner(point, corners.index(point))
    elif point[0] in [0, r] or point[1] in [0, c]:
        if point[0] == 0:
            return edge(point, index)
        elif point[1] == 0:
            index += 2
            return edge(point, index)
        elif point[0] == r:
            index += 1
            return edge(point, index)
        else:
            index += 3
            return edge(point, index)

    else:
        return middle(point)





for _ in xrange(int(raw_input())):
    rows, cols = map(int, raw_input().split())
    points = dict()
    pos = dict()
    for i in xrange(rows):
        lst = map(int, raw_input().split())
        for j in xrange(cols):
            if lst[j] == 1:
                points[(i,j)] = 1
            else:
                points[(i,j)] = 0
    r = rows - 1
    c = cols - 1
    edges = dict()
    for point in [i for i in points.keys() if points[i] == 1]:
        edges[point] = (position(r,c,point))

    q = deque()
    grouped = []
    count = []
    for point in [i for i in points.keys() if points[i] == 1]:
        troop = []
        if point not in grouped:
            q.append(point)
            troop.append(point)
            grouped.append(point)

            while len(q) > 0:
                a = q.popleft()
                if len(edges[a]) <= 0:
                    break
                for i in edges[a]:
                    if i not in troop:
                        q.append(i)
                        troop.append(i)
                        grouped.append(i)
            count.append(len(troop))

    print '{0} {1}'.format(len(count), max(count))




































