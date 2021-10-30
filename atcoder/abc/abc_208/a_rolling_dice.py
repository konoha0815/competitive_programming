A, B = map(int, input().split())

min = A
max = A*6

if max >= B >= min:
    print("Yes")
else:
    print("No")