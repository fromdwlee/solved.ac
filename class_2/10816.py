import sys
N = int(sys.stdin.readline())
card_num = list(map(int, sys.stdin.readline().split()[:N]))
M = int(sys.stdin.readline())
check_num = list(map(int, sys.stdin.readline().split()[:M]))

card_dict = {}
for num in card_num:
    if num in card_dict:
        card_dict[num] += 1
    else:
        card_dict[num] = 1

result = [card_dict[num] if num in card_dict else 0 for num in check_num]

print(' '.join(map(str, result)))