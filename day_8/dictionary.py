# example of dictionary

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(len(person))

print(person['first_name'])
print(person['skills'][0])

try:
  print(person['city'])
except:
  print("city key value not present in the person dictionary")
  
person['city'] = "chennai"
person['first_name'] = "shyamanth"

print('city' in person)

"""
removing key value pairs from dictionary
pop('city')
popitem() -> returns the last key
del person['last_name'] removes the last_name key value pair

"""
person_lst = person.items()
print(person_lst)


person_cpy = person.copy()


# to remove the entire dictionary
person.clear()
del person

key = person_cpy.keys()
value = person_cpy.values()

