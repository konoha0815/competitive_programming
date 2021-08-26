N = int(input())

for i in reversed(range(60)):
    if 2**i <= N:
        print(i)
        break



N = int(input())

for i in range(60-1, 20-1, -1):
    if 2**i <= N:
        print(i)
        break

########################################

# N = int(input())

# for i in range(0, 60):
#     if 2**i > N:
#         print(i - 1)
#         break
