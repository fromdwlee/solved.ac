import sys
A, B = [], []
N, M = map(int, sys.stdin.readline().split())

for i in range(N):
    i = list(map(int, sys.stdin.readline().split()))
    A.append(i)

for i in range(N):
    i = list(map(int, sys.stdin.readline().split()))
    B.append(i)

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=' ')
    print()
