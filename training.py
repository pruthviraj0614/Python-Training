'''L=[]
for x in range(1,12):
 L.append(x**2)
print(L)

L=[x for x in range(1,20) if (x%2==0)]
print(L)

#constructer 
class Student:
   def __init__(self,rollno,name):
     self.rollno=rollno
     self.name=name
   def __string__ (self):
      return f"rollno:{self.rollno} name:{self.name}"
   
#trial
a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=3
result = (a[c] * (b[c]^2)//2) %3
print(result)

#atm
class ATM:
    def __init__(self, balance=0, pin="1234"):
        self.balance = balance
        self.pin = pin

    def verify_pin(self):
        entered_pin = input("Enter your 4-digit PIN: ")
        return entered_pin == self.pin

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Enter a valid amount to deposit.")

def main():
    atm = ATM(balance=1000, pin="1234")
    print("Welcome to the ATM")
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        if atm.verify_pin():
            print("PIN verified successfully.\n")
            break
        else:
            attempts += 1
            print(f"Incorrect PIN. Attempts remaining: {max_attempts - attempts}")

    if attempts == max_attempts:
        print("Too many incorrect attempts. Card blocked.")
        return

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                atm.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 3.")


if __name__ == "__main__":
    main()
'''   

'''#practice
a=10
print(type(a))   
print(dir(a))
''' 
'''a="pruthviraj"
print(a[-1::-1])
print(a[7:10])
print(a[0:7])
print(a[6::-1])
'''

'''a="Pruthviraj"
print(a.lower())
print(a.upper())
'''

'''def palindrome(p):
    return p==p[ ::-1]
word=input("enter the word")
print(palindrome(word))
'''
'''num=int(input(print("Enter the num")))
if(num%2==0):
    print("the num is even")
else:
    print("the num is odd")  
'''      
'''a=input(print("enter palindrome:"))
if(a==a[::-1]):
    print("true")
else:
    print("false") 
'''       
'''a=int(input("enter 1st num:"))
b=int(input("enter 2st num:"))
c=a+b
print(f"addition of a={a} and b={b} is {c} ")
'''
#16\7\25
'''class employe:
    def __init__(self,eid,ename,add):
        self.eid=eid
        self.add=add
class address:
  def __init__(self,fno,city,pin):
        self.fno=fno
        self.city=city
        self.pin=pin
  def __str__(self):
        return f"flat no:{self.fno}, city:{self.city},pin:{self.pin}"  
add=address(22,"solapur",413219)
e1=employe(1,"koli",add)
print((e1.add.pin)) 
'''

i = 1
while(i <= 10):
    print(i)
    i = i + 3    
    i = i - 2 

#class 1
'''class Product:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    def show_product_info(self): 
        print(f"Product: {self.name}")
        print(f"Brand: {self.brand}")
        print(f"Price: ₹{self.price}")

#class 2
class PhoneFeatures:
    def __init__(self, camera, battery, storage):
        self.camera = camera
        self.battery = battery
        self.storage = storage

    def show_features(self):
        print(f"Camera: {self.camera} MP")
        print(f"Battery: {self.battery} mAh")
        print(f"Storage: {self.storage} GB")
class MobilePhone(Product, PhoneFeatures):
    def __init__(self, name, brand, price, camera, battery, storage):
        Product.__init__(self, name, brand, price)
        PhoneFeatures.__init__(self, camera, battery, storage)

    def show_full_details(self):
        self.show_product_info()
        self.show_features()
phone = MobilePhone("Galaxy A15", "Samsung", 79999, 108, 5000, 256)
phone.show_full_details()
'''
'''a=10
b=0
def div(a,b):
    try: 
        print(a/b)
    except ZeroDivisionError:
        print("non zero")
div(a,b)
'''
#threading
'''
import threading
def sq(N):
    print(N*N)
t1=threading.Thread(target=sq,args=(5, ))
t1.start()
  

import threading
def p1():
    for i in range(3):
        print("first")
t1=threading.Thread(target=p1)
t1.start()  

#increment, global value/ global variable?   
'''