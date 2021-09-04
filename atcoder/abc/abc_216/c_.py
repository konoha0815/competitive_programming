N = int(input())

x = bin(N)[2:]
ans = ""
for c in x:
    ans += 'B'
    if c == '1':
        ans += 'A'

print(ans)

########################################

# N = int(input())

# ans = ""


# while N != 0:
#     while N % 2 == 0:
#         ans += "B"
#         N //= 2
    
#     while N % 2 != 0:
#         ans += "A"
#         N -= 1

# length_str = len(ans)
# sliced_ans = ans[length_str -1::-1]
# print(sliced_ans)

# print(ans[::-1])


    
