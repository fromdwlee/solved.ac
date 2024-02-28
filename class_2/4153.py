while True:
    N = list(map(int, input().split()))
    N.sort()
    
    if N[0] == 0 & N[1] == 0 & N[2] == 0:
        break
    if (N[0]**2 + N[1]**2) == N[2]**2:
        print("right")
    else:
        print("wrong")