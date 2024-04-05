K, N = map(int, (input().split()))

num_list = []

for _ in range(K):
    num = int(input())
    num_list.append(num)

start, end = 1, max(num_list)

result = 0
while start <= end:
    mid = (start + end) // 2
    count = sum(x // mid for x in num_list)

    if count >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)