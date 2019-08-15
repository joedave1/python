class Node:
    def __init__(self,dataa):
        self.data=dataa
        self.nxt=None
class ll:
    def __init__(self):
        self.head=None
        
    def insertbeg(self,nd):
        nn=Node(nd)
        nn.nxt=self.head
        self.head=nn
        
    
    def insertatend(self,nd):
        nn=Node(nd)
        if self.head is None:
            self.head=nn
            return
        last=self.head
        while last.nxt:
            last=last.nxt
        last.nxt=nn
    
    def insertatmid(self,nd,mid):
        nn=Node(nd)
        nn.nxt=mid.nxt
        mid.nxt=nn
        
    def delatbeg(self):
        temp=self.head
        self.head=temp.nxt
        temp.nxt=None
            
    
    def display(self):
        temp=self.head
        while temp.nxt!=None:
            print(temp.data," ==> ",end='')
            temp=temp.nxt
        print(temp.data)   
        
llob=ll()
ch=0
print("LinkedList Implementation")
while ch<=5:
    print("1.Insert    2.Delete   3.Display    4.Insert at End   5.Insert at Middle")
    ch=int(input())
    if ch==1:
        a=input("Enter a value : ")
        llob.insertbeg(a)
        llob.display()
        
    elif ch==2:
        llob.delatbeg()
        llob.display()
    elif ch==3:
        llob.display()
        
    elif ch==4:
        a=input("Enter a value : ")
        llob.insertatend(a)
        llob.display()
    elif ch==5:
        a=input("Enter a new node : ")
        b=input("Enter the mid node: ")
        llob.insertatmid(a,b)
        llob.display()     
