S, T = (map(str, input().split()))

before_list = [S, T]

after_list = sorted(before_list)

if before_list == after_list:
    print("Yes")
else:
    print("No")

