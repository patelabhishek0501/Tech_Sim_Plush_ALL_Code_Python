class Car:
    def __init__(self,name,model):

        self.name = name
        self.model = model

    def move(self):
            print("Driven")

class Boat:
    def __init__(self,name,model):

        self.name = name
        self.model = model

    def move(self):
            print("Sail")

class Plane:
    def __init__(self,name,model):

        self.name = name
        self.model = model

    def move(self):
            print("Fly")

Car1 = Car("Farari","Rai")
Boat1 = Boat("Top Model","Ram")
Plane1 = Plane("Rafhel","Sayam")
for x in (Car1,Boat1,Plane1):
 x.move()