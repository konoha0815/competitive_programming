N, M = map(int, input().split())
A = [list(map(int, input().split())) for l in range(M)]

def janken(a_hand, b_hand):
    if a_hand == b_hand:
        return "d"

    if a_hand == "G" :
        if b_hand == "C":
            return "a"
        elif b_hand == "P":
            return "b"

    if a_hand == "C":
        if b_hand == "P":
            return "a"
        elif b_hand == "G":
            return "b"

    if a_hand == "P":
        if b_hand == "G":
            return "a"
        elif b_hand == "C":
            return "b"

for i in A:
    i


for i in range(M):
    for j in range(N):
        A[1][M]



    
