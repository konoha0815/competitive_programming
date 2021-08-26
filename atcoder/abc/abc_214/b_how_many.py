S, T = input().split()
S = int(S)
T = int(T)
ans = 0

for a in range(101):
    for b in range(101):
        for c in range(101):
            if a + b + c <= S and a*b*c <= T:
                ans += 1
print(ans)

        
