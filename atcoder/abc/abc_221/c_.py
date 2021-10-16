import math
from itertools import permutations

N = input()

N_list = []

G_1 = 0
G_2 = 0

for i in N:
    N_list += i



if len(N)%2==0:
    G_1 = len(N)/2
    G_2 = len(N)/2
else:
    G_1 = math.ceil(len(N)/2)
    G_2 = int(len(N)/2)

base_1 = list(permutations(N, len(N)))
base_list =[]

for i in base_1:
    i = ''.join(i)
    base_list.append(i)

ans = 0
for i in base_list:
    A = i[:int(G_1)-1]
    B = i[int(G_1):]
    print(A)
    print(B)

    if A[0] != "0" and B[0] != "0":
        C = int(A)*int(B)
        print(C)
        if ans < C:
            ans = C

print(C)
        


# for i in base_1:
#     for j in base_2:
#         if sorted(i + j) == sorted(N_list):
#             a = (i, j)
#             base_list.append(a)


# print(base_list)


