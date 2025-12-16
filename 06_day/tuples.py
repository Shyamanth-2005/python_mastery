tpl = ('ball','pen','pencil','eraser')
fruits = ('orange','apple','grape','mango','banana','lemon')
# accessing the elements  can be done by index it can be both positive and negative indexing
last_fruit = fruits[-1]
first_fruit = fruits[0] # indexing starts with 0

# slicing can also be done to get a part of the tuple

first_three_fruits = fruits[:3]
print(first_three_fruits)

# change tuple to list

lst =  list(tpl)

 # item in tpl -> returns true or false 
 
 # joining  tuples


tpl1 = (1,2,3,4)
tpl2 = (4,5,6,7)
tpl3 = tpl1+tpl2
print(tpl3)

# we can't change any element in tuple (immutable)

# deleting tuples : we can't delete a single element in tuple but we can delete the entire tuple 

del tpl1

family = ('father','mother','sibling1','sibling2')
father,mother,*siblings = family

fruits = ('mango','apple','orange')
vegetable=('cabbage','potato','onion')
animal = ('cat','dog','cow')
food_stuff_tp = fruits + vegetable + animal
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
middle_item_idx = len(food_stuff_lt) // 2
middle_item = food_stuff_lt[middle_item_idx]

first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print(last_three_items)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

