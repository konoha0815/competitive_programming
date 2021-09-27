N = int(input())
A = list(map(int, input().split()))
X = int(input())

lcount = 0
count = 0
another = 0
A_sum = 0
ans_sum =0
ans_count = 0

for i in A:
    count += 1
    A_sum += i

lcount = X//A_sum
another = X%A_sum

count = count*lcount

for i in A:
    ans_sum += i
    ans_count += 1
    if another < ans_sum:
        print(count+ans_count)
        exit()
    
