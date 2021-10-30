P = int(input())

coin = 1
coins = []
count = 0
for i in range(1,11):
    coin = coin*i
    coins.append(coin)

coins.reverse()


for i in coins:
    for j in range(1, 101):
        if P - i*j < 0:
            count += j-1
            P = P - i*(j-1)
            break
        elif P - i*j == 0:
            count += j
            print(count)
            exit()
