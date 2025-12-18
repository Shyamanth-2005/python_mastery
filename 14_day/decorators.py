"""
a decorator is a design pattern that can be used to add new feature on an exsisting function without changing its internal structure

"""

# Normal function

def greeting():
  return "Welcome to python"

def upper_case_decoration(function):
  def wrapper():
    func = function()
    make_uppercase = func.upper()
    return make_uppercase
  return wrapper
g = upper_case_decoration(greeting)
print(g())


def upper_case_decorator(function):
  def wrapper():
    func = function()
    make_uppercase = func.upper()
    return make_uppercase
  return wrapper

@upper_case_decorator
def greeting():
  return "Welcome shyamanth"

print(greeting())


