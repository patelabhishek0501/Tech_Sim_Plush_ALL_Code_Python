# class Mobile():
#      def features(self,ram,ram1 ):
#           print(self,ram,ram1)
       
          
# obj = Mobile()

# obj.features("","hi")

############################################################
# class Mobile():
#     def features(self):
#         print("Madhav")

# obj = Mobile()

# obj.features("hi")
###########################################################
# class Mobile():
#     def features(obj):
#         print("Inside",obj)

# obj = Mobile()

# print("Outside",obj)

# obj.features()
########################################################
# class Mobile():
#     def features(obj):
#         print("Inside",obj)

#         frontC = "5px"
#         backC = "25px"
#         name = "Nokia"

#         obj.front_Camera = frontC
#         obj.back_Camera = backC
#         obj.Model_Name = name

# obj = Mobile()

# obj.features("56","45","67")
# obj2 = Mobile()
# obj2.features("55px","25px","JIO")
# class Person:
#     age = 20
#     def setAge(self, age):
#         self.age = age
#     def getAge(self):
#        print(self)
# person = Person()
# Person2 = Person()
# print(person.age)


class Game:
    power = 5
    def getPower(self):
        self.power -= 1
    def onAttack(self):
        self.power  += 1

    def checkPower(self):
        if(self.power == 0):
            print("Game Over")

game = Game()

game.onAttack()
game.onAttack()
game.onAttack()
game.checkPower()
print(game.onAttack())


