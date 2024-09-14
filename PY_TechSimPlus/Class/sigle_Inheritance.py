class A:
    def __init__(self):
        print("init A")
    def Method1(self):
        print("Method1")
    def Method2(self):
        print("Method2")


class B(A):
    def __init__(self):
        print("initB")
        super().__init__()
    def Method1B(self):
        print("MethodB1")
    def Method2B(self):
        print("MethodB2")



class C(B):
    def __init__(self):
        print("initC")
        super().__init__()
    def Method2C(self):
        print("MethodC1")
    # B.__init__()   

c = C()
c.Method2C()
