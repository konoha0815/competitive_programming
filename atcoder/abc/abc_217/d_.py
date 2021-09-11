L, Q = list(map(int, input().split()))
Query_list = []
for i in range(Q):
    C, X = map(int, input().split())
    Query_list.append([C, X])

# wood = list(range(1, L + 1)
wood = []
for k in range(L + 1):
    wood.append(k)
 

ans_list = [0, L]
count = 0

for j in Query_list:
    if j[0] == 1:
        ans_list.append(wood[j[1]])
        ans_list = sorted(ans_list)
    elif j[0] == 2:
        for l in range(len(ans_list)):
            if ans_list[l] > wood[j[1]]:
                print(ans_list[l] - ans_list[l - 1])
                break


