n = int(input())

n_list = list(map(int, input().split()[:n]))

print(min(n_list), max(n_list))