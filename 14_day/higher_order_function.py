# function inside a function 

# or function passed as parameter to another function

def sum_numbers(nums):
  return sum(nums)


def higher_order_function(f,lst):
  summation = f(lst)
  return summation

result = higher_order_function(sum_numbers,[1,2,3,4,5])

print(result)


def square(x):
  return x**2
def cube(x):
  return x**3
def absolute(x):
  if x < 0:
    return -x
  return x  
# cube  = lambda x : x**3

# print(absolute(2))

def hof(type):
  match(type):
    case "square":
      return square
    case "cube":
      return cube
    case "absolute":
      return absolute
result = hof("cube")
print(result(3))

result = hof("absolute")
print(result(-32))

