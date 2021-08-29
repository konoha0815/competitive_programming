N = int(input())

S = [0] * N
T = [0] * N
for i in range(N):
    S[i], T[i] = map(str, input().split())

name = list(zip(S, T))

if len(name) == len(set(name)):
    print("No")
else:
    print("Yes")
