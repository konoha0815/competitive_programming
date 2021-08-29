N = int(input())

ans = ""

if N == 0:
    print("B")
    exit()


if N > 0 :
    while N != 0:
        while N % 2 == 0:
            ans += "B"
            N //= 2
        
        while N % 2 != 0:
            ans += "A"
            N -= 1

length_str = len(ans)
sliced_ans = ans[length_str::-1]
print(sliced_ans)


    
