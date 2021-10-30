A, B = map(int, input().split())

# print((A-B)/3+B)

C = B-A+1
if C <= 0:
    print("0")
else:
    print(C)

