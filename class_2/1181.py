N = int(input())

word_list = []

for i in range(N):
    word_list.append(input())

result = list(set(word_list))

result.sort()
result.sort(key=len)
print(*result, sep="\n")