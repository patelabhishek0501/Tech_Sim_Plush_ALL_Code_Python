class First:
    def First_Class(self):
        print("First_Class")
class Second(First):
    def Sec_Class(self):
        print("Second_Class")
class Third:
    def Third_Class(self):
        print("Third_Class")
class Fourth(Third,Second):
    def Fourth_Class(self):
        print("Fourth_Class")

Sec = Second()
Four = Fourth()
Sec.First_Class()
Sec.Sec_Class()
Four.Third_Class()
Four.Fourth_Class()