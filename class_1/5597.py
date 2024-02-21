import sys
n = [int(sys.stdin.readline()) for _ in range(28)]

check = sorted(range(1, 31))

for i in check:
    if i not in n:
        print(i)
