class First:
    def __init__(self):
        print("init1")
    def First_ClassA(self):
        print("First_ClassA")

    def First_ClassA(self):
        print("First_ClassA")
    
    def First_Class2(self):
        print("First_ClassA")

class Sec:
    def __init__(self):
        print("init2")
    def Sec_ClassB(self):
        print("Sec_ClassB")
    
    def Sec_Class1B(self):
        print("Sec_Class1B")
    
    def Sec_Class2B(self):
        print("Sec_Class2B")

class Third():
    def __init__(self):
        print("init3")
       
        First.__init__(self)
        Sec.__init__(self)
    def Third_ClassC(self):
        print("SecThird_ClassC")
    
    def Third_Class1C(self):
        print("SecThird_Class1C")
    
    def Third_Class2C(self):
        print("SecThird_Class2C")

class Fourth(Sec,Third):
    def __init__(self):
        print("init3")
       
        First.__init__(self)
        Sec.__init__(self)
    def Third_ClassD(self):
        print("SecThird_ClassD")
    
    def Third_Class1D(self):
        print("SecThird_Class1D")
    
    def Third_Class2D(self):
        print("SecThird_Class2D")


