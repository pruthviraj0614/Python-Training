class Stack:
    def __init__(self):
        self.container=[]
    def Isempty(self):
        return len(self.container)==0 
    def push(self,data):
        self.container.append(data)
    def pop(self):
        if self.Isempty():
            print('stack is empty')
        else:
            return self.container.pop()
    def peek(self):
         return self.container[-1] 
    def Isfull(self):
        if len(self.container)>=4:   #try for max_size (homework)
            print('stack full')
        else:
            return 'not full', len(self.container)     
     
obj=Stack()
print(obj.Isempty()) 
print(obj.push(44))   
print(obj.push(84))
print(obj.push(94))
print(obj.Isempty())
print(obj.pop())
print(obj.peek())
print(obj.container)
print(obj.Isfull()) 

