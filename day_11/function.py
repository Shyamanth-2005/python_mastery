class Book:
  def __init__(self):
    self.books = []
  def get_book_details(self):
    book = dict()
    
def generate_full_name(first_name,last_name):
  print(f"{first_name} {last_name}")

def sum_of_all_numbers(*nums):
  sum = 0
  for num in nums:
    sum += num
  print(sum)
def team_display(team_number,*team_members):
  print(team_number)
  print("team members",end=": ")
  for team_member in team_members:
    if team_member != team_members[-1]:
      print(team_member,end=" ,")
    else:
      print(team_member)

def get_number():
  number = int(input())
  return number
# function inside a function
def square_number(function_get_number):
  number  = function_get_number() 
  return number * number

def reverse_list(arr):
  n = len(arr)-1
  mid = n//2
  for i in range(mid):
    temp  = arr[n-i]
    arr[n-i] = arr[i]
    arr[i] = temp
  print(arr)

def check_all_dtype_same(arr):
  dtype_set = set()
  for element in arr:
    if type(element) not in dtype_set:
      dtype_set.add(type(element))
  if len(dtype_set) > 1:
    return False
  return True

if __name__ =="__main__":
  
  generate_full_name(first_name="shyamanth",last_name="reddy")
  
  sum_of_all_numbers(2,3,4)

  team_display("team1","shyamanth","hari","mohan","yash","sai")
  
  print(square_number(get_number))
  
  reverse_list([1,2,3,4,5])

  print(check_all_dtype_same([1,"1",23,True]))
