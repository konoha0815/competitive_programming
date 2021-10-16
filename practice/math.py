a = 200
b = 160

for i in range (211):
    if (a*i + 3600)%7200 == 0 and (b*i)%7200 == 0:
        print(i)
      