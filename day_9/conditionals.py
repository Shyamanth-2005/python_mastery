def question1():
  age  = int(input("Enter your age: "))
  print("You are old enough to learn to drive.") if age >= 18 else print(f"You need {18-age} more years to learn to drive")

def question2():
  my_age = 25
  your_age = int(input("Enter your age: "))
  if your_age > my_age:
    diff_age = your_age - my_age
    if diff_age == 1:
      print(f"You are {diff_age} year older than me")
    else:
      print(f"You are {diff_age} years older than me")
    
if __name__ =="__main__":
  question1()
  
  person={
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
  
  person_skills = person['skills']
  if 'JavaScript' in person_skills and 'React' in person_skills:
    print("front-end developer")