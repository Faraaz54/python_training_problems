def position(r,c, point):
    lst = []
    if point[0] in [0, r] and point[1] in [0, c]:
        corners = [(0, 0), (0, c), (r, 0), (r, c)]
        for i in corners:
            if i == point:
                return ['corner', corners.index(i)]
    elif point[0] in [0,r] or point[1] in [0,c]:
        edges = [0,r,c]
        for i in [point[0],point[1]]:
            if i in edges:
                return ['edge', edges.index(i)]


lst = position(54,48, 36)

print lst