from data.countries import countries

count = 0
# while and while - else extension
while count < 5:
  print(count)
  count +=1
else:
  print(count)


count = 0

while count < 5:
  count+=1
  if count == 3:
    break
  
count = 0
while count < 5:
  if count == 3:
    count +=1
    continue
  print(count)
  count +=1
else:
  print(count)

numbers = [0, 1, 2, 3, 4, 5]

for number in numbers:
  print(numbers.index(number))
  
lang = 'python'
for char in lang:
  print(char)
  
for i in range(len(lang)):
  print(lang[i])

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

for key in person:
  print(key)
for key,value in person.items():
  print(key,end= " : ")
  print(value)
  
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

for company in it_companies:
  print(company)

numbers = (0,1,2,3,4,5)
for number in numbers:
  print(number)
  if number == 3:
    break
else:
  print("Over")
  
# range(start,end,skip)

for number in range(0,11,2):
  print(number,end=" ")
  
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person:
  if key == "skills":
    for skill in person["skills"]:
      print(skill,end=" ")
for number in range(6):
  pass
print(countries)