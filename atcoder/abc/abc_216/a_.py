XY = input()

str_list = list(XY)
X = int(float(XY))

if 2 >= int(str_list[-1]) >= 0:
    print(str(X)+"-")
elif 6 >= int(str_list[-1]) >= 3:
    print(str(X))
else:
    print(str(X)+"+")
 