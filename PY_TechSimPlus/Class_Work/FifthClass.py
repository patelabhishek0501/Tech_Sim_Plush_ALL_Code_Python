# # x = "Hello"
# s = input("Enter the string::")
# input()
# li = list(s)
# print(li)
# new = []
# for i in s:
#     print(i)
#     char = li.pop(0)
#     li.append(char)
#     print(char)
#     print(li)
#     j = ''.join(li)
#     new.append(j)
#     print(''.join(),(li))

# numbers = []

# one = int(input("Enter the first num to add in list "))
# numbers.append(one)

# two = int(input("Enter the first num to add in list "))
# numbers.append(two)

# three = int(input("Enter the first num to add in list "))
# numbers.append(three)
# fourth = int(input("Enter the first num to add in list "))
# numbers.append(fourth)
# print(numbers)

# li = list(numbers)
# print(li)
##############################################################
# li = []
# for i in range(5):
#   num = int(input("Enter any number: "))
#     # li.append(num)
# # print(sum(li))

# add = 0
# for i in li:
#     add = add + li 
#     print(add)
###############################################################
# li = [34,4,56,67,56,67,9]

# for i in range(len(li)):
    
#     print(li[i])
###############################################################

# li = [1,34,56,2,7,8,9,8]
# find = 6

# for i in li:
#     if i < 0:
#         print("is a negative value")
#         break

# li = [1,2,6,7,8,9,0,8,7,5,6,7]

# for i in li:
#     if i == 3:
#         continue
#     print(i)

###############################################################
# av = 5
# num = int(input("Enter the number"))

# for i in range(num):
#     if i == av:
#         print("out of stock")
#         break
#     else:
#         print("candy")

###################homework###############################
    # *******
    # ******
    # *****
    # ****
    # ***
    # **
    # *

##########################Ans###################
# height = 6
# width = 6
# for i in range(height):
#     for j in range(width-i):
#         print('*',end='')
# # Move to the next line after each row
#     print()
####################Second problem#########################
        #  ********
        #   ******
        #    ****
        #     **
        #      *
########################Second problem Ans#################
height = 7
for i in range(height):
    for j in range(i):
        print(' ',end='')
    for k in range((height-i)*2):
        print('*',end='')
    print()