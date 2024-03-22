import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    cnt = list(range(1, n+1))
    for i in range(k):
        for j in range(1, n):
            cnt[j] += cnt[j-1]
    print(cnt[-1])