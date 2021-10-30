N , X = map(int, input().split())
A = list(map(int, input().split()))

price = 0
for i in range(len(A)):
    if i % 2 == 0:
        price += A[i]
    else:
        price += A[i]-1

if X - price >= 0:
    print("Yes")
else:
    print("No")

    
