import math
class Calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def sum(self):
        print(f"Sum is {self.x+self.y}")

    def difference(self):
        print(f"Difference is {self.x-self.y}")

    def product(self):
        print(f"Product is {self.x*self.y}")

    def division(self):
        if(self.y == 0):
            print("Error: Division by 0 is not allowed.")
        else:
            print(f"Division is {self.x/self.y}")
    
    def exponential(self):
        print(f"Exponential is {self.x**self.y}")

    def remainder(self):
        if(self.y ==0):
            print("Error: Division by 0 is not allowed.")
        else:
            print(f"Remainder is {math.pow(self.x,self.y)}")

my_calculator = Calculator(2,4)
my_calculator.sum()
my_calculator.difference()
my_calculator.product()
my_calculator.division()
my_calculator.exponential()
my_calculator.remainder()