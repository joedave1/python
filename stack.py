class Stack:
    
    def __init__(self):
        self.stack=[]
        
    def add(self,dataval):
        if(dataval not in self.stack):
            self.stack.append(dataval)
            return True
        else:
            return False
            
    def peek(self):
        return self.stack[-1]
    
    def remove(self):
        if(len(self.stack)<=0):
            return("no element")
        else:
            return self.stack.pop()
    def print(self):
        print(self.stack)
a=Stack()
a.add(4)
a.add(12)
a.add("python stack")
a.add(8)
print(a.peek())
a.remove()
a.print()