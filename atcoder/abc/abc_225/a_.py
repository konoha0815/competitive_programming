S = input()

A = []

for x in S:
    A.append(x)

A = set(A)

if len(A) == 1:
    print("1")
elif len(A) == 2:
    print("3")
else:
    print("6")



