# import random

# N, X = map(int, input().split())

# A = [random.randint(1, N) for _ in range(N)]

# result = [num for num in A if num < X]
# print(result)

N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")