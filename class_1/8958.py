T = int(input())

for i in range(T):
    a = str(input())
    score = 0
    sum_score = 0

    for x in range(len(a)):
        if a[x] == "O":
            score += 1
            sum_score += score
        else:
            score = 0

    print(sum_score)