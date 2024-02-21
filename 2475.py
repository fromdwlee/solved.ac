A, B, C, D, E = map(int, input().split())

A_square = pow(A,2)
B_square = pow(B,2)
C_square = pow(C,2)
D_square = pow(D,2)
E_square = pow(E,2)

result = (A_square+B_square+C_square+D_square+E_square)%10

print(result)