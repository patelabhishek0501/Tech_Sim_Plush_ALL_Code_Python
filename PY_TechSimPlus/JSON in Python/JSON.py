# If you have a JSON string, you can parse it by using the json.loads() method.

import json

x = '{"name":"Abhishek","age":23,"Year":2023}'

y = json.loads(x)

print(y["age"])

# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

x1 = {
   "age" : 23,
   "name":"Abhishek Patel",
   "Year":2024
}

y1 = json.dumps(x1)

print(y1)
#############################Convert Python objects into JSON strings, and print the values:#############################
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

x2 = {"age":22,"name":"Abhishek","Year":2024}
y3 = json.dumps(x2)
print(y3)

x4 = ["Banana","orange","Grapes"]
y4 = json.dumps(x4)
print(y4)

x5 = ("Ram","Shayam","Radhe")
y5 = json.dumps(x5)
print(y5)

x6 = "Abhishek"
y6 = json.dumps(x6)
print(y6)

x7 = 789
y7 = json.dumps(x7)
print(y7)

x8 = 78.9
y8 = json.dumps(x8)
print(y8)

x9 = True
y9 = json.dumps(x9)
print(y9)

x10 = False
y10 = json.dumps(x10)
print(y10)

x11 = None
y11 = json.dumps(x11)
print(y10)


e = {
     "name" : "Abhishek",
     "age" : 30,
    "divorced":False,
    "married":True,
    "pets" :None,
    "children":("ismile","Love"),
     "car":[
  {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
     ]
 }
y67 = json.dumps(e)
print(y67)

# Use the indent parameter to define the numbers of indents:
print(json.dumps(e, indent=4))


# Use the separators parameter to change the default separator:
print(json.dumps(x, indent=4, separators=(". ", " = ")))


# Use the sort_keys parameter to specify if the result should be sorted or not:

print(json.dumps(x, indent=4, sort_keys=True))