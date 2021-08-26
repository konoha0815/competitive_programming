N = int(input())
A = list(map(int, input().split()))

A_pick = sorted(A)[N - 2]
print(A.index(A_pick) + 1)