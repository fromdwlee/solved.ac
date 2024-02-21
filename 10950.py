T = int(input())
results = []

for i in range(T):
    a, b = map(int, input().split())
    result = a+b
    results.append(result)
    
for result in results:
    print(result)