class Vehical:
    def __init__(self,Model,Name):
        self.Model = Model
        self.Name = Name
    def Move(self):
        print("Driven")

class Car(Vehical):
    pass

class Boat(Vehical):
    def Move(self):
        print("sail")

class Plane(Vehical):
    def Move(self):
     print("Fly")

Car1 = Car("ModelFar","Farari")
Boat1 = Boat("Monilika","Monika1")
Plane1 = Plane("Rafel","Rafel1")

for x in(Car1 , Boat1 , Plane1):
    print(x.Model)
    print(x.Name)
    x.Move()
 


