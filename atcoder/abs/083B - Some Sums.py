N, A, B = list(map(int, input().split()))
def list_sum(n):
    s = str(n)
    array = list(map(int, s))
    return sum(array)

ans = 0
for i in range(1, N + 1):
        if B >= list_sum(i) >= A:
            ans += i

print(ans)


