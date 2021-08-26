N = int(input())

for i in range(1,10):
    if N%i == 0:
        for s in range(1,10):
            if N/i/s == 1:
                print("Yes")
                exit()
    
print("No")
        

