import sys
N = int(sys.stdin.readline())
point = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    point.append((x, y))

point.sort(key=lambda x : (x[0], x[1]))

for xy in point:
    print(*xy)