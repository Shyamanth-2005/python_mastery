"""
Syntax error:
try:
  print "Hello world"
except Exception as e:
  print(f"{e}")

"""

# name error -> we debug the error by defining the variable name
try:
  print(age)
except Exception as e:
  print(f"{e}")
  
# Index Error -> just make sure the index number u use is less than the length of the array

try:
  arr = [1,2,3,4]
  print(arr[7])
except Exception as e:
  print(f"Error: {e}")

  
# ModuleNotFoundError -> this happens when there is no such module or library that exsists 

try:
  import maths
except Exception as e:
  print(f"Error : {e}")

# attribute error -> means that no such function does not exsists in the module , lets fix it by changing the proper name of that function

try:
  import math
  math.PI # we can try math.pi instead
except Exception as e:
  print(f"Error: {e}")

# key error -> arises when there is no such that exists or there might be typo in the key
try:
  users = {"name":"shyamanth","age":20,"country":"india"}
  print(users["coutry"])  
except Exception as e:
  print(f"Error: {e}")
  
# type error -> is rised because we can't  add a number to string or vice -versa we have to convert them to similar type and then
# perform the operation

try:
  print('4' + 3)
except Exception as e:
  print(f"Error: {e}")
  
# Import Error -> it arises if no such function is exsists in the module

try:
  from math import power
except Exception as e:
  print(f"Error: {e}")
  
# Value Error ->  we can't change the given  string to number , because of  a letter

try:
  int('12a')
except Exception as e:
  print(f"Error: {e}")


# Zero Division Error ->    We can't divide a number by 0

try:
  1/0
except Exception as e:
  print(f"Error: {e}")
  