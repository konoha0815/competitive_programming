N = int(input())
A = list(map(int, input().split()))

A = sorted(A, reverse=True)

Alice_ans = 0
Bob_ans = 0

Alice = list(A[0: N: 2])
Bob = list(A[1: N: 2])

for i in Alice:
    Alice_ans += i    

for j in Bob:
    Bob_ans += j

ans = abs(Alice_ans - Bob_ans)

print(ans)

