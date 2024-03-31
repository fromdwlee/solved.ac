import sys
input = sys.stdin.readline

K = int(input())
num_list = []

for _ in range(K):
    num = int(input())
    if num == 0:
        del num_list[-1]
    else:
        num_list.append(num)

print(sum(num_list))