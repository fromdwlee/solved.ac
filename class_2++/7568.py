N = int(input())

hw = [list(map(int, input().split())) for _ in range(N)]

for i in hw:
    rank = 1
    for j in hw:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")