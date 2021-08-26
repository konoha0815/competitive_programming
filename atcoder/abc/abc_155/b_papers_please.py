N = int(input())
A = list(map(int, input().split()))

even = 0
even_correct = 0
for a in A:
    if a % 2 == 0:
        even += 1
        if a % 3 == 0 or a % 5 == 0:
            even_correct += 1

if even == even_correct:
    print("APPROVED")
else:
    print("DENIED")    


