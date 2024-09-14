class First:
    def __init__(self):
        print("init1")
    def First_Class(self):
        print("First_Class")

    def First_Class1(self):
        print("First_Class1")
    
    def First_Class2(self):
        print("First_Class2")

class Sec:
    def __init__(self):
        print("init2")
    def Sec_Class(self):
        print("Sec_Class")
    
    def Sec_Class1(self):
        print("Sec_Class1")
    
    def Sec_Class2(self):
        print("Sec_Class2")

class Third(First,Sec):
    def __init__(self):
        print("init3")
       
        First.__init__(self)
        Sec.__init__(self)
    def Third_Class(self):
        print("SecThird_Class")
    
    def Third_Class1(self):
        print("SecThird_Class1")
    
    def Third_Class2(self):
        print("SecThird_Class2")


T=Third()
