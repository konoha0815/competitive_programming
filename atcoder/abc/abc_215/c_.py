import itertools

S, K= input().split()
K = int(K)

list_S = list()
p = itertools.permutations(S, len(S))

for i in p:
    list_S.append("".join(i))
list_S = sorted(set(list_S))

print(list_S[K - 1])


########################################

# import itertools

# S, K= input().split()

# list_S = list()
# all = itertools.permutations(S, len(S))

# for i in all:
#     #print(i)
#     list_S.append("".join(i))
# list_S = set(list_S)
# list_S = sorted(list_S)

# print(list_S[int(K) - 1])




