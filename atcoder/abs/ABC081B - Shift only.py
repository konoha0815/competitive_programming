def count_two(num):
    count = 0
    while num % 2 == 0:
        count += 1
        num //= 2
    return count

n = int(input())
a = [int(m) for m in input().split(" ")]

print(min([count_two(a_i) for a_i in a]))

########################################

# N = int(input())
# A = list(map(int, input().split()))

# list_count = []

# for i in A:
#     for j in range(1, 31, -1):
#         if i%(2**j) == 0:
#             list_count.append(j)
            

# print(min(list_count))


       
