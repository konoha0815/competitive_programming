A, B, C = map(int, input().split())

for i in range(10**5):
    if B >= C*i >= A:
        print(C*i)
        exit()
    elif C*i > B:
        print("-1")
        exit()
    