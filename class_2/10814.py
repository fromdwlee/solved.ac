N = int(input())
users = []

for i in range(N):
    info = input()
    age, name = info.split()
    age = int(age)
    users.append((age, name))

users.sort(key=lambda x : x[0])

for user in users:
    print(*user)