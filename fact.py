num=int(input("Enter a number: "))
fact=1
if num==0:
    print("factorial is 1")
elif num>0:
    for i in range(1,num+1):
        fact=fact*i
        print(fact)
else:
    print("sorry there's no factorial for this number")
