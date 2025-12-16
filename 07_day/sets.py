st = set()
st = {'item1','item2','item3'}

# accessing the elements can be done through a loop

# checking if an element is there or not is done by 'in'

print(f"is the item1 present in the set st? {'item1' in st}")

# adding an element to the set

st.add('item4')

# addding multiple elements in set

st.update(['item5','item6','item7'])

# remove a perticular element from the set

st.remove('item1')

# pop a random element

item = st.pop()

# if we want to clear or empty the set we use clear()

st.clear()

# if you want to delete the entire set

del st

# convert list to set
lst = ['item1', 'item2', 'item3', 'item4', 'item1']

st = set(lst)

"""
Joining the sets:
  1. Union -> if you need a new set with all the elements from the two other sets then use it
  2. update -> if you need to add the elements in the second set to the first set without creating a new set then use this
"""

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

# intersetion

st4 = st1.intersection(st2)

# superset and subset
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}

st2.issubset(st1)
st1.issuperset(st2)

st1.difference(st2)

# symmetric difference = (A\B) U (B\A)

st2.symmetric_difference(st1)

# to check if common element is present or not , if no common element it returns true  else false


st2.isdisjoint(st1)
