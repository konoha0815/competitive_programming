N = int(input())
S, T = input().split()

ans = ""
for n in range(N):
    ans += S[n] + T[n]    
print(ans)

