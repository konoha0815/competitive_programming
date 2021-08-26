N = int(input())
D = list(map(int, input().split()))

a = 0
b = 0

for i in D:
    a += i*i
    for j in D:
            b += i*j

ans = (b - a)/2
        
print(int(ans))