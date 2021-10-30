N, M = map(int,input().split()) 
B = [list(map(int, input().split())) for l in range(N)]

if B[0][0] % 7 == 0 and M != 1:
    print("No")
    exit() 

if 7 - B[0][0]%7 + 1 >= M:

    for i in range(N):
        for j in range(M-1):
            if B[i][j+1] - B[i][j] != 1:
                print("No")
                exit()

    for i in range (N-1):
        if B[i+1][0] - B[i][0] != 7:
            print("No")
            exit()

    print("Yes")
else:
    print("No")
