def My_Fun():
  x = "Hi"
  
  def My_Fun1():
   nonlocal x
   x ="Hello"
  My_Fun1()
  return x
print(My_Fun())
           
