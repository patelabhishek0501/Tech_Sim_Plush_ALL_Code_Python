# class Abhi:
#     def __init__(self):
#         self.college = "BGI"
#         print("I Am Calling")
    
#     def setName(self,name):
#         self.name = name
    
#     def getName(self):
#         print(self.name)
    
# p1 = Abhi()
# print(p1.college)

class Circle:
  def __init__(self,radius):
    self.radius = radius

  def getArea(self):
     return 3.14*self.radius*self.radius 

p1 = Circle(2)
print(p1.getArea())


