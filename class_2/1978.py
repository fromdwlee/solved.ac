N = int(input())
n_list = list(map(int, input().split()[:N]))

result = 0

for i in range(N):
    if n_list[i] == 1:
        continue
    is_prime = True

    for x in range(2, int(n_list[i]**0.5) + 1):
        if n_list[i] % x == 0:
            is_prime = False
            break
    if is_prime:
        result += 1

print(result)