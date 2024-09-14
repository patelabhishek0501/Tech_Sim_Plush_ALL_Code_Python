# print(numbers.append(100))
#numbers.extend([12,43,43])
# print(numbers)
#numbers.remove(43)
#print(numbers)
# op= numbers.pop()
# print(op)
# print(numbers)
# val= numbers.count(45)
# print(val)
# num= numbers.index(78)
# print(num)
# numbers.sort()
# print(numbers)
# numbers.reverse()
# numbers.sort(reverse=True)/// givs value in descending order
# print(numbers)

#--------------store a given value on a certain position-----------------
 #var1=int(input ("Enter the value "))
# pos=int(input ("input the position "))
# numbers.insert(pos,var1)
# print(numbers)
#----------------------------------------------------------------------
#////A number is 
numbers = [23,34,45,78,74,63]
pos=int(input ("input the position "))
print(numbers[pos])
numbers.remove(numbers[pos])