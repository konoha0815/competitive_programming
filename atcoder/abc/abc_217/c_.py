N = int(input())
P = list(map(int, input().split()))

ans = []
for i, name in enumerate(P, 1):
    a_list = [i, name]
    ans.append(a_list[::-1])

ans = sorted(ans)
f_ans = []
for j in ans:
    k = j[1]
    f_ans.append(k)


print(*f_ans)
