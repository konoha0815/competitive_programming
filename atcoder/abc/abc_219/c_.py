X = input()
N = int(input())
S = [input() for _ in range(N)]
alp = "abcdefghijklmnopqrstuvwxyz"
alp = alp.upper()

inv = []
for k in S:
    for i in range(26):
        k = k.replace(X[i], alp[i])
    inv.append(k)

inv = sorted(inv)

ans = []
for k in inv:
    for i in range(26):
        k = k.replace(alp[i], X[i] )
    ans.append(k)

for i in ans:
    print(i)
    






# S_max = 0
# for a in range(len(S)):
#     if len(S[a]) > S_max:
#         S_max = len(S[a])

# ans = []
# for i, j in enumerate(X, 1):
#     for b in range(len(S)):
#         for k in range(S_max):
#             if j == S[b][k]

#         if S[k] == j:

# for j in range(len(S)):
#     if i == S[j][0]:
#         ans.append(S[j])

# print(ans)

