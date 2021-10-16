S = input()
T = input()

if S == T:
    print("Yes")
    exit()

T_0 = ""

for i in range(len(S)-1):
    T_0 = T[:i] + T[i+1] + T[i] + T[i+2:]
    if S == T_0:
        print("Yes")
        exit()

print("No")



