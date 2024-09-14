# Display numbers divisible by 5 from a list
# numbers = [10, 20, 33, 46, 55]

# numbers = [10,20,33,46,55]
# for  number in numbers:
#     if numbers%5==0:
#         print(number)
#     else:
#         print("list in value not aviable whose divisible by 5")

#######################when take value user###############################
# num =  input("Enter the number seperate space")

# li = (int(y) for y in num.split())

# for lis in li:
#  if lis%5==0:
#   print([lis])
#  else:
#   print("Number is a not present") 

##########################different logic using Append###################

num = input("Enter the number")

li = (int(x) for x in num.split())

lin = []

for lis in li:
    if lis%5==0:
        lin.append(lis)
else:
     print(f"{lis}is not a divisible")
print("it is a divisible 5",lin)

