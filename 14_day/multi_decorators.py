# first decorator
def uppercase_decorator(function):
  def wrapper():
    func =  function()
    make_upper_case = func.upper()
    return make_upper_case
  return wrapper

# second decorator
def split_string_decorator(function):
  def wrapper():
    func = function()
    make_split_string = func.split()
    return make_split_string
  return wrapper

@split_string_decorator
@uppercase_decorator  # order of decorators are important as they can affect the overall output 
def greeting():
  return "Hi Shyamanth"
print(greeting())

"""
Error:
.upper() attribute not available for the list if uppercase_decorator was above split_string_decorator
"""


# decorators with parameters

def decorators_with_parameter(function):
  def wrapper(para_1,para_2,para_3):
    function(para_1,para_2,para_3)
    print("I am {} and i go to {} and i stay at {}".format(para_1,para_2,para_3))
  return wrapper
@decorators_with_parameter
def get_full_name(first_name,middle_name,last_name):
  return f"{first_name} {middle_name} {last_name}"
print(get_full_name("shyamanth","reddy","medapati"))

# decorators generally override the exsisting function with the new functionality provided by the decorators
