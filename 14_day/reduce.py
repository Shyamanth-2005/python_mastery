from functools import reduce
"""
Like map and filter it takes two parameters a function and a iterable however instead of returning 
a iterable it returns a single term and it needs to be imported from functools 

"""

numbers_str = ['1','2','3','4','5']

def add_two_num(x,y):
  return int(x) + int (y)

def mul_two_num(x,y):
  return int(x) * int(y)
result = reduce(add_two_num,numbers_str)
result_mul = reduce(mul_two_num,numbers_str)

print(result)
print(result_mul)