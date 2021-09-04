S1 = input()
S2 = input()
S3 = input()

contest = ["ABC", "ARC", "AGC", "AHC"]

contest.remove(S1)
contest.remove(S2)
contest.remove(S3)

for i in contest:
    print(i)