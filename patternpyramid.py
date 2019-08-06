def pattern(n):
    for i in range(0,n):
        for k in range(n,i,-1):
            print(" ",end="")
        for j in range (0,i+1):
            print("*",end=" ")
        print("\r")
        
n=int(input())
pattern(n)
