student = {
    "name" : "Abhi",
    "age" :"21",
    "add":{
       "city":{
          "name" : "bhopal" 
       }
    }
}
print(student["add"]["city"]["name"])
op = student.keys()
print(op)
print(student.values())
print(student.items())
