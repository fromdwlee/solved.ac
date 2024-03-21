import sys
input = sys.stdin.readline

L = int(input())
string = list(input().strip())
M = 1234567891

result = 0

for i in range(L):
    num = ord(string[i])-96
    hashfunc = num * 31**i
    result += hashfunc

print(result % M)