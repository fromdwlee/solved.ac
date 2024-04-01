from collections import deque
import sys
import math

input = sys.stdin.readline

n = int(input())

trim = math.floor((n*0.15) + 0.5)

level = []

for _ in range(n):
    level.append(int(input()))

level.sort()
q = deque(level)

for _ in range(trim):
    q.popleft()
    q.pop()
    
if len(q) == 0:
    result = 0
    print(result)
else:
    result = math.floor((sum(q)/len(q))+0.5) 
    print(result)