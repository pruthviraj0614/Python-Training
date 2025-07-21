#1
'''class a:
    pass
obj=a()
print(obj)

#2
class a:
    def func():
        print('chavan')
obj=a()
obj.func() 
'''
#3
'''class a:
    def func(self):
        print('chavan')
obj=a()
print(obj.func()) 
#obj and self are same .
'''
#4
'''class a:
    def a(self):
        a=10
        print(a)
obj=a()  
print(obj.a()) 
'''
#5
'''class a:
    def __init__(self):
        print('gm')
obj=a()
'''

#6
'''class a:
    def __init__(self,m):
        print('gm',m)
obj=a()
'''

#7
'''class a:
    def __init__(self):
        print(id(self))
obj=a()
print((id(obj)))
'''
#8
'''class a:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
        print(name,roll,marks)
obj=a('pruthviraj',69,501)        
'''
#9
'''class a:
    def __init__(self,name):
        self.name=name
obj1=a('vivan')
print(obj1.name)
obj2=a('koli')
print(obj2.name)
obj1.__init__ ('prithviraj')        #constructor called out
print(obj1.name)
'''
#10
'''class student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
        print(id(self))

    def talk(self):
        print('hello my name is',self.name)
        print('hello my roll is',self.roll)   
        print('hello my marks is',self.marks)
obj=student('koli',69,502)
obj.talk() 
'''
#11 variables
'''class a:
    class_var="i am a class variable"
    def show_variables(self):
        local_var="i am a local var"
        self.instance_var="i am an instance var"
        print("class_var:",a.class_var)
        print("local_var:",local_var)
        print("self instance_var:",self.instance_var)
obj=a()
obj.show_variables()
'''
#12  static method
'''class student:
    def greet():
        print('hello')
student.greet()
'''
#13
'''class rectangle:
    def __init__ (self):
        self.l=10
        self.b=20
class cuboid(rectangle):
    def __init__(self):
       # rectangle.__init__(self)  #calling parent class constructor
        super().__init__()         # or this can also be used
        self.h=30 
    def volume(self):
        print('vol of couboid is', self.l*self.b*self.h) 
obj=cuboid()
obj.volume()  
'''
#linear search 
a=[1,2,3,4,5]
Tar=3
for i in range(len(a)):
    if a[i]==Tar:
        print('target found',a)
        break 
else:
    print('not found')

