filename = input("Enter the file name")

check_dotPosition = filename.rfind('.')

if check_dotPosition != -1:
   extension = filename[check_dotPosition+1:]
   print(f"file extension:{extension}")
else:
   print("file is not a extensions")
  