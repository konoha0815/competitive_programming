# N = int(input())
# l = [list(map(int, input().split())) for l in range(N-1)]

# sum_l = []
# for i in range(len(l)):
#     i = sum(l[i])
#     sum_l.append(i)


# for i in range(1,N+1):
#     ans_list = [i]
#     for j in sum_l:
#         k = j - i
#         if k <= 0:
#             print("No")
#             exit()
#         else:
#             ans_list.append(k)
#     if len(set(ans_list)) == N:
#         print("Yes")
#         exit()
    
# print("No")

import collections

N = int(input())
l = [list(map(int, input().split())) for l in range(N-1)]

flat_list = []
for t in l:
    for u in t:
        flat_list.append(u)


cc = collections.Counter(flat_list)
ans_list = [x for x in flat_list if cc[x] > 1]


if len(set(ans_list)) == 1:
    print("Yes")
else:
    print("No")
        