class Node:
    def __init__(self,dataval=None):
        self.data=dataval
        self.next=None
        
class SlinkedList:
    def __init__(self):
        self.headval=None
        
    def listprint(self):
        temp=self.headval
        while temp:
            print(temp.data,"==>",end='')
            temp=temp.next
            class Node:
    def __init__(self,dataval=None):
        self.data=dataval
        self.next=None
        
class SlinkedList:
    def __init__(self):
        self.headval=None
        
    def listprint(self):
        temp=self.headval
        while temp:
            print(temp.data,"==>",end='')
            temp=temp.next
            
    def atbegin(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.headval
        self.headval=newnode
        
    def delete(self):
        d=self.headval
        self.head=self.headval.nextval
        d.next=None
        
ll=SlinkedList()

ch=0
while ch<4:
    print("1. insertion 2.deletion 3.display 4.exit")
    ch=int(input("enter the choice"))
    if ch==1:
        print("enter")
        a=input()
        ll.atbegin(a)
        ll.listprint()
    elif ch==2:class Node:
    def __init__(self,dataval=None):
        self.data=dataval
        self.next=None
        
class SlinkedList:
    def __init__(self):
        self.headval=None
        
    def listprint(self):
        temp=self.headval
        while temp:
            print(temp.data,"==>",end='')
            temp=temp.next
            
    def atbegin(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.headval
        self.headval=newnode
        
    def delete(self):
        d=self.headval
        self.head=self.headval.nextval
        d.next=None
        
ll=SlinkedList()

ch=0
while ch<4:
    print("1. insertion 2.deletion 3.display 4.exit")
    ch=int(input("enter the choice"))
    if ch==1:
        print("enter")
        a=input()
        ll.atbegin(a)
        ll.listprint()
    elif ch==2:
        ll.delete()
        
    elif ch==3:
        ll.listprint()
    else:
        print(" invalid ")


        ll.delete()
        
    elif ch==3:
        ll.listprint()
    else:
        print(" invalid ")


    def atbegin(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.headval
        self.headval=newnode
        
    def delete(self):
        d=self.headval
        self.head=self.headval.nextval
        d.next=None
        
ll=SlinkedList()

ch=0
while ch<4:
    print("1. insertion 2.deletion 3.display 4.exit")
    ch=int(input("enter the choice"))
    if ch==1:
        print("enter")
        a=input()
        ll.atbegin(a)
        ll.listprint()
    elif ch==2:
        ll.delete()
        
    elif ch==3:
        ll.listprint()
    else:
        print(" invalid ")

