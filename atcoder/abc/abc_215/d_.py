import sympy as sym

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

j_list = []
for i in A:
    for j in range(1, M + 1):
        if sym.gcd(i, j) == 1:
            j_list.append(j)


            

