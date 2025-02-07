class Sushma:
    location = "itahari"
    def __init__(self,id):
        self.id = id
        print(f"{self.id}")

    def slogan(self):
        return "best IT College"   
    
college = Sushma(100)
print(college.slogan())        