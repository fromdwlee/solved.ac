a, b = map(int, input().split())

for i in range(min(a,b), 0, -1):
    if a%i == 0 and b%i == 0:
        gcd = i
        print(gcd)
        break

lcm = a*b//gcd
print(lcm)