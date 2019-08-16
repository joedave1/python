class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def Printtree(self):
        print(self.data)
root=node(10)
root.Printtree()
