from collections import deque
import sys

input = sys.stdin.readline

d = deque()
n = int(input())

for i in range(n):
    command = input().split()

    if command[0] == "push":
        d.appendleft(command[1])
    elif command[0] == "pop":
        if len(d) == 0:
            print("-1")
        else: print(d.popleft())
    elif command[0] == "size":
        print(len(d))
    elif command[0] == "empty":
        if len(d) == 0:
            print("1")
        else: print("0")
    elif command[0] == "top":
        if len(d) == 0:
            print("-1")
        else: print(d[0])
