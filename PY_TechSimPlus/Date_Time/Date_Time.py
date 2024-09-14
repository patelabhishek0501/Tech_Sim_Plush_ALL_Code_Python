import datetime #these are a in built it is a contain Year , Month , Date,Second, microSecond

x = datetime.datetime.now()
print(x)
######################################
# year , Week
print(x.year)
print(x.strftime("%A"))
#######################################
# formate given argument
# Creating Date Objects
z =datetime.datetime(2024,7,12) 
print(z)

# The strftime() Method

c = datetime.datetime(2024,4,1)

print(c.strftime("%A"))
print(c.strftime("%B"))