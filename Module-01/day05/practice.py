
#quation No1


#Vehicle base class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def describe(self):
        print(f"{self.make} : {self.model}")
    
class Car(Vehicle):
    def __init__(self,make,model):
        super().__init__(make,model)
        
    def describe(self):
        print(f" {self.make} :{self.model}") 


from abc import abstractmethod

class Truck(Vehicle):

    @abstractmethod

    def __init__(self,make,model):
        super().__init__(make,model)
        
    def describe(self):
        print(f"{self.make} and {self.model}")
    def wheels(self):
        ...
vehicles = [
    Truck("Ford", "F-150"),
    Car("Honda", "Civic"),
    Truck("Chevrolet", "Silverado 1500"),
    Car("BYD", "Seal"),
    Truck("Ram", "1500"),
    Car("Subaru", "Outback"),
    Truck("GMC", "Sierra 1500"),
    Car("Tesla", "Model 3"),
    Truck("Nissan", "Frontier"),
    Car("BYD", "Atto 3")
]    

for vehicle in vehicles:
    vehicle.describe()


#crate sub class frm truck class

class Two_While_Truck(Truck):
    def __init__(self,make,model):
        super().__init__(make,model)
    
    def wheel(self):
        return f" this {self.model} is 2 Wheel Truck's "

class Four_While_Truck(Truck):
    def __init__(self,make,model):
        super().__init__(make,model)
    
    def wheel(self):
        return f" this {self.model} is 4 Wheel Truck's "
#nwe line for abstract sub class test
print("\n\n\n")

#check Polymorphism working in abstract wheel method
Isuzu = Two_While_Truck("Isuzu", "NPR")
Ford = Four_While_Truck("Ford","F-650")

for vec in [Isuzu, Ford]:
    print(vec.wheel())