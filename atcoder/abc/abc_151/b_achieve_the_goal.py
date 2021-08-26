N, K, M = map(int, input().split())
A = list(map(int, input().split()))

ans = sum(A)

m = (M*N - ans)

if 100 >= m >= 0:
    print(m)
elif 0 > m:
    print("0")
else:
    print("-1")
########################################
# N, K, M = map(int, input().split())
# A = list(map(int, input().split()))

# ans = 0

# for a in A:
#     ans += a

# m = (M*N - ans)

# if 100 >= m >= 0:
#     print(m)
# elif 0 > m:
#     print("0")
# else:
#     print("-1")


########################################

# N, K, M = map(int, input().split())
# A = list(map(int, input().split()))

# ans = 0

# for a in A:
#     ans += a

# list_m = [m for m in range(101) if ans + m >= N*M]
        
# if len(list_m) >= 1:
#     print(min(list_m))
# else:
#     print("-1")

