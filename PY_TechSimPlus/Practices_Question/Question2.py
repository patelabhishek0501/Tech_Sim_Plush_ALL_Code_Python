student = {
    "name" : "Alice",
    "age"  :  "20",
    "grade":  " "   
}

if("grade") is student:
    print("ABC")

else: 
    print("Grade is a not present")

g = student.get("grade","garde not present")

print(g)


