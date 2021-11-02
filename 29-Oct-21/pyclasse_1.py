
# ------------------
# -----CLASS -------
# ------------------

# --------------------
# create class for dog
#-----------------------
class dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print(f"Hi I am {self.name} and I'm {self.age} years old")
    def addweight(self,weight):
        self.weight = weight
    def changename(self,name):
        self.name = name
    def displayinf(self):
        print(f"Hi I am {self.name} and I'm {self.age} years old")  

tim = dog('tim', 12)

tim.speak()
tim.changename('ferdo')
tim.displayinf()

# ---inhirit ----
class cat(dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
alco = cat('alaco', 8, 'gray')
alco.speak()


# --------------------
# create class for CAR
# --------------------
class car(object):
    def __init__(self, make, model, year, kms, aircondtion):
        self.make = make
        self.model = model
        self.year = year
        self.aircondtion=aircondtion
        self.kms = kms
    def display(self, showAll):
        if showAll:
            print(f"this car has {self.make}\n{self.model}\n{self.year}\n{self.aircondtion}")
        else:
            print(f"this car has {self.make}\n{self.model}\n{self.year}\n")

carwip = car('Ford', 'Fujen', 2012, 'Yes', 0)
carwip.display(True)