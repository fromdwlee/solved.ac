from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
num_list = []

for _ in range(N):
    num = int(input())
    num_list.append(num)

num_list.sort()

print(round(sum(num_list)/N))
print(num_list[N//2])

cnt = Counter(num_list).most_common()
if len(cnt) > 1 and cnt[0][1]==cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(max(num_list)-min(num_list))