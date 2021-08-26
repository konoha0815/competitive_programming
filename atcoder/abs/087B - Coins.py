A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0
for h in range(A + 1):
    for i in range(B + 1):
        for j in range(C + 1):
            if h*500 + i*100 + j*50 == X:
                ans += 1

print(ans)
