N = int(input())

def factorial(N):
    if N == 0:
        return 1
    return N * factorial(N-1)

result = str(factorial(N))

cnt = 0

while result[-1] == "0":
    result = result[:-1]
    cnt += 1
    if result[-1] != "0":
        break

print(cnt)