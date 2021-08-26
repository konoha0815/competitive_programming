X = input()

if int(X)%1111 == 0:
    print("Weak")
elif 0 <= int(X[0]) <= 6:
    if int(X[0]) == int(X[1]) - 1 == int(X[2]) - 2 == int(X[3]) - 3:
        print("Weak")
    else:
        print("Strong")
elif X == "7890" or X == "8901" or X == "9012":
    print("Weak")
else:
    print("Strong")
