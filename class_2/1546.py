N = int(input())
score = list(map(int, input().split()[:N]))

score.sort()

new_score = []

for i in range(len(score)):
    new_score.append(score[i]/score[-1]*100)

print(sum(new_score)/len(new_score))