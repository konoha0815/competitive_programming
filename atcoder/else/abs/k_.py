N = int(input())
t = [0] * N
x = [0] * N
y = [0] * N
for i in range(N):
    t[i], x[i], y[i] = map(int, input().split())

t.insert(0, 0)
x.insert(0, 0)
y.insert(0, 0)

print(t, x, y)
for j in range(N - 1):
    print((t[j+1] - t[j]) - (x[j+1] - x[j]) - (y[j+1] - y[j]))
    print(0%2)
    if (t[j+1] - t[j]) - (x[j+1] - x[j]) - (y[j+1] - y[j]) >= 0 and (t[j+1] - t[j]) - (x[j+1] - x[j]) - (y[j+1] - y[j])%2 == 0:
        print("True")
    else:
        print("No")
        exit()

print("Yes")
