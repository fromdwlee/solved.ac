import sys
n = [int(sys.stdin.readline()) for _ in range(10)]

re_list = []

for i in range(len(n)):
    re = n[i]%42
    re_list.append(re)

x = []

for i in re_list:
    if i not in x:
        x.append(i)

print(len(x))