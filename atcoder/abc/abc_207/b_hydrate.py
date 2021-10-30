A, B, C, D = list(map(int, input().split()))

if B >= C*D:
    print("-1")
    exit()
else:
    for i in range(100001):
        if A + B*i <= C*D*i:
            print(i)
            exit()
