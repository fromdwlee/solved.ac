N = int(input())

layer = 1
while N > 1 + 3*layer*(layer-1):
    layer += 1
print(layer)