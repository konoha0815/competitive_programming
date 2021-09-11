P = list(map(int, input().split()))

A = "abcdefghijklmnopqrstuvwxyz"
ans = ""
for i in P:
    ans += A[i-1]

print(ans)



