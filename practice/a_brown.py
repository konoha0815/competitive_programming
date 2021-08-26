# print("hello world")

# input: 入力
# S = input()

# # print: 出力
# print(S)

# # [start:stop:step]
# print(S[::-1])

# a = 31
# b = 89
# c = 7
# d = 19

# # a += b:  a = a+b
# a += b
# c -= d

# print(a, c)

# a += b
# c -= d

# print(a, c)

# print(a+b)
# print(c-a*b)
# print(c**c)
# print(b/d)
# # //割ったときの商
# print(31//7)
# # %は割ったときのあまり
# print(31%7)

# age = 20
# point = int(input("点数を入力してください："))

# if age >= 100:
#     print("too old")

# if age >= 20:
#     print("yes")
# else:
#     print("no") 

# if point >= 90:
#     print("秀")
# elif 90 > point >= 80:
#     print("優")
# elif 80 > point >= 70:
#     print("良")
# elif 70 > point >= 60:
#     print("可")
# else:
#     print("不可")


# if point >= 90:
#     print("秀")
# elif point >= 80:
#     print("優")
# elif point >= 70:
#     print("良")
# elif point >= 60:
#     print("可")
# else:
#     print("不可")

# n番目のフィボナッチ数を return する関数 (高速でない)
# def fib(n):
#     if n == 0 or n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)

# for i in range(12):
#     print(i, fib(i))

# x = 10
# ans = 0
# for i in range(x+1):
#     ans += i

# print(ans)


# x = 256
# t = ""
# while x != 0:
#     r = x % 2
#     t += str(r)
#     x //= 2
# ans = t[::-1]
# print(x, ans)

# name = ["", "r","t",""]
# print("a".join(name))

# ↓文字列
# a = "今日の"
# b = "天気は"
# c = "雨です"

# print(a+b+c)
# print(b+c+a)


# str = "supercalifragilisticexpialidocious"

# print(str[0:5],str[9:13],str[14:18])

# x = 3.14
 
# print(x, type(x))

# x = 9**(1/3)

# print(x, type(x))

# a = [2, 3, 5, 7, 11, 13]
# print(a, type(a), len(a))

# a.append(17)
# print(a, len(a))

# a.pop(2)
# print(a, len(a))
# a.pop()
# print(a, len(a))

# print(a[1::2])

b = [[1, 2, 3], [4, 5, 6, 7], 8]
print(b, len(b))
print(b[0], len(b[0]))
print(b[0][2], type(b[0][2]))