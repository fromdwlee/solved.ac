N, K = map(int, input().split())

def factorial(N):
    if N == 0:
        return 1
    return N * factorial(N-1)

print(factorial(N) // (factorial(K) * factorial(N - K)))