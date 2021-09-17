import numpy as np

M = int(input())
a = [list(map(str, input().split())) for l in range(M)]
b = [list(map(str, input().split())) for l in range(M)]
a_array = []
b_array = []
# a.replace(".", 0).replace("#", 1)
for i in range(M):
    a_array.append(list(a[i][0]))

for j in range(M):
    b_array.append(list(b[i][0]))


for k in range(25):
    for l in range(4):
        a_array = np.roll(a_array, k)
        a_array = np.rot90(a_array, l)
        if a_array & b_array:
            print("Yes")
            exit

print("No")
        