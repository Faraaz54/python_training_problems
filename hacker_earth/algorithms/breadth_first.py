from collections import deque
import sys

scan = sys.stdin


def main():
    test = int(scan.readline())
    for t in range(test):
        n, m = map(int, scan.readline().split())
        tree = []
        for i in range(n):
            tree.append([])
        for i in range(m):
            x, y = map(int, scan.readline().split())
            tree[x - 1].append(y - 1)
            tree[y - 1].append(x - 1)
        # print tree
        level = [0] * n
        q = deque()
        q.append(0)
        level[0] = 0
        while len(q) > 0:
            a = q.popleft()
            if a == n - 1:
                break
            for i in tree[a]:
                if i != 0 and level[i] == 0:
                    q.append(i)
                    level[i] = level[a] + 1
        print level[n - 1]


main()