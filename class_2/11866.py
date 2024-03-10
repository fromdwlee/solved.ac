N, K = map(int,(input().split()))

N_list = list(range(1, N+1))

pop_list = []

index = 0

while N_list:
    index = (index + K - 1) % len(N_list)
    pop_list.append(str(N_list.pop(index)))

print("<" + ", ".join(pop_list) + ">")