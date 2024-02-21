n = int(input())

num = str(input())

if len(num) == n:
    print(sum(map(int, num)))
else:
    print("범위 초과")