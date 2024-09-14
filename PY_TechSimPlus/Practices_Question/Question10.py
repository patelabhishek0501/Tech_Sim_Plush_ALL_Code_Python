
numbers = input("Enter the number to Seperate Space")
str_list = [f' {num}' for num in numbers]
str_tuple = tuple(str_list)
print(f"List: {str_list}")
print(f"Tuple: {str_tuple}")