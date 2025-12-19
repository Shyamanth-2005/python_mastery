"""
syntax
map(function,iterable)
"""

def mod_26(x):
  return x % 26

lst = [27,25,25,27]
lst = list(map(lambda x : x%26,lst))
print(lst)


number_str = ['1','2','3','4','5']
number_lst = list(map(int,number_str))
print(number_lst)


names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

print(list(map(lambda name:name.upper(),names)))