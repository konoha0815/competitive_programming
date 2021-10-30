S1 = input()
S2 = input()
S3 = input()
S4 = input()

S_list = [S1, S2, S3, S4]
ans_list = ["H", "2B", "3B", "HR"]

if sorted(S_list) == sorted(ans_list):
    print("Yes")
else:
    print("No")