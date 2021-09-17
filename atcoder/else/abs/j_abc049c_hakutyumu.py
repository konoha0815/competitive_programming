S = input()

while len(S) != 0:
    if S[-5::] == "dream":
        S = S[:len(S)-5]
    elif S[-5::] == "erase":
        S = S[:len(S)-5]
    elif S[-6::] == "eraser":
        S = S[:len(S)-6]
    elif S[-7::] == "dreamer":
        S = S[:len(S)-7]
    else:
        print("NO")
        exit()

print("YES")

