def pattern(n):
    for i in range(0,n):
        for k in range (i):
            print(" ",end="")
        for j in range (0,n-i):
            print("*",end="")
        print("\r")
        
n=int(input())
pattern(n)
