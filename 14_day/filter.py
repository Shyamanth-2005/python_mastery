"""
syntax
filter(function,syntax)

"""

numbers = [1,2,3,4,5]

is_even = lambda x : x % 2 == 0

is_odd = lambda x : x % 2 != 0

def is_name_long(name):
  if len(name) > 7:
    return True
  return False

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']


print(list(filter(is_even,numbers)))
print(list(filter(is_odd,numbers)))
print(list(filter(is_name_long,names)))