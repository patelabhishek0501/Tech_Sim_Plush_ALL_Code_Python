import Var_Modul
Var_Modul.Person["age"] = 13
a = Var_Modul.Person["age"]
print(a)

#Renaming Modual

import Var_Modul as mx

b = mx.Person["Name"]

print(b)
# Import only the person dictionary from the module:
from Var_Modul import Person
print(Person["age"])
