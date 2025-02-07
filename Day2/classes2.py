#Basics of Classes in python

class Car:
    def __init__(self,brand,model,price): #Constructor
        self.brand = brand # Attribute
        self.model = model
        self.price = price
        self.speed = 0

    def display_features(self):
            print(f"Brand: {self.brand}\nModel: {self.model}\nPrice: {self.price}")
    
    def sound(self):
         print("Vrrrrrrrrrr !!!!")

    def accelerate(self,value):
         self.speed += value
         print(f"The {self.model} is now at {self.speed}km/hr.")
    
    def brake(self,value):
         self.speed = max(0,self.speed-value)
         print(f"The {self.model} is slowed down to {self.speed}km/hr.")
      
tesla = Car(brand="Tesla",model="CyberTruck",price="$200K")
tesla.display_features()
tesla.sound()
tesla.accelerate(100)
tesla.brake(50)

print("\n")

# Inheritance in Classes(Reusing code)
class Vehicle:
     def __init__(self,model):
          self.model = model
    
     def honking(self):
        print(f"{self.model} is honking 🚗📢")

class Bike(Vehicle):
     def __init__(self, model,price):
          super().__init__(model)#super() is used to inherit the constructor from the parent. 
          self.model = model
          self.price = price
     def aboutBike(self):
          print(f"This is {self.model} and costs {self.price} USD.")

hayabusa = Bike(model="Hayabusa",price="140K")
hayabusa.aboutBike()
hayabusa.honking()

print("\n")

# Encapsulation(Data Hiding)
class Bank:
     def __init__(self,balance):
          self.__balance = balance # Private variable
     def deposit(self,amount):
          self.__balance += amount
     def check_balance(self):
          print(f"You have Rs.{self.__balance} in your account.")

nabil_bank = Bank(200000)
nabil_bank.deposit(10000) #you can not directly access "balance" i.e. it can not be changed easily. It is technically hidden.
nabil_bank.check_balance()

print("\n")

#Polymorphism
class Truck(Vehicle): #Polymorphism is method overriding but not just method overriding.
     def __init__(self, model):
          super().__init__(model)
     def honking(self):
          print(f"{self.model} is saying Balle Balle !!")

my_truck = Truck("Truck R1")
my_truck.honking()