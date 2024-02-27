S = input()
alpha = list(map(chr, range(97,123)))

for s in alpha:
    found = False
    for i in range(len(S)):
        if s == S[i]:
            print(i, end=" ")
            found = True
            break
    if not found:
        print("-1", end=" ")