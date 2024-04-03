T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    pri = list(map(int, (input().split())))[:N]
    result = 1
    while pri:
        if pri[0] < max(pri):
            pri.append(pri.pop(0))
        else:
            if M == 0:
                break
            pri.pop(0)
            result += 1
        M = M - 1 if M > 0 else len(pri) - 1
    print(result)