M, N = map(int, (input().split()))

sieve = [True] * (N+1)
sieve[0], sieve[1] = False, False

sqrt = int(N**0.5)

for i in range (2, sqrt+1):
    if sieve[i] == True:
        for j in range(i+i, N+1, i):
            sieve[j] = False

result = [i for i in range(max(2,M), N+1) if sieve[i] == True]
print(*result, sep='\n')