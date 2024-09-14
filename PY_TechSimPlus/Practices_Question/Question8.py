
def is_Palidrome(num):
    num_str1 = str(num)
    rver_str1 = num_str1[::-1]

    if(num_str1==rver_str1):
        return True
    else:
        return False
number = input("Enter the number")

if is_Palidrome(number):
    print("number is a palidrome")
else:
    print("number is a not palidrme")


