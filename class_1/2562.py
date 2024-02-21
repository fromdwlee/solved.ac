import sys
n = [int(sys.stdin.readline()) for _ in range(9)]

max_num = max(n)

print(max_num)
print(n.index(max_num)+1)