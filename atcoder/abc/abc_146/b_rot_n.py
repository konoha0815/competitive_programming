N = int(input())
S = input()

ans =""
for s in S:
    ans += chr(ord("A") + (ord(s) - ord("A") + N )%26)
print(ans)
