class BST:
    def __init__(self,key):
        self.lchild=None
        self.rchild=None
        self.key=key
    def insert(self,data):
       if data<self.key:
           if self.lchild:
               self.lchild.insert(data)
           else:
               self.lchild=BST(data) 
       elif data>self.key:
           if self.rchild:
               self.rchild.insert(data)
           else:
               self.rchild=BST(data)
root=BST(10)
root.insert(20)
root.insert(5)
print(root.lchild.key) 
print(root.rchild.key)               



           
                             