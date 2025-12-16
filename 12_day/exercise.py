import string
from random import randint

def random_user_id():
  characters  = ""
  characters += string.ascii_letters
  characters += string.digits
  user_id = ""
  for _ in range(6):
    user_id += characters[randint(0,len(characters)-1)]
  
  print(user_id)

# random_user_id()


def user_id_gen_by_user_id():
  len_char , len_line = list(map(int,input().split()))
  character_space = string.ascii_letters + string.digits
  for _ in range(len_line):
    user_id = ""
    for _ in range(len_char):
      user_id += character_space[randint(0,len(character_space)-1)]
    print(user_id)

user_id_gen_by_user_id()