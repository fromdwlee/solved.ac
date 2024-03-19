import sys
input = sys.stdin.readline
N = int(input())

digit = 0

M=N

while(M):
    M //= 10
    digit += 1

start_num = N - (digit*9)
start_num = max(start_num, 0)

for i in range(start_num, N+1):
    num = sum(map(int,str(i)))
    num_sum = i + num
    if num_sum == N:
        print(i)
        break
    elif i == N:
        print(0)