N, M = map(int,(input().split()))
card_num = list(map(int, input().split()[:N]))

result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if card_num[i] + card_num[j] + card_num[k] > M:
                continue
            else:
                result = max(result, card_num[i] + card_num[j] + card_num[k])

print(result)