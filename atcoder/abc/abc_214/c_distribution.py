N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

for i in S:
    T[0] += i
    print(T)
