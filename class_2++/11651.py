import sys
N = int(sys.stdin.readline())
point = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    point.append((x, y))

point.sort(key=lambda y : (y[1], y[0]))

for xy in point:
    print(*xy)