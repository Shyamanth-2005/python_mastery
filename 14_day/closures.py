def add_ten():
  ten = 10
  def add():
    ten_2 = 10
    def add_twice(num):
      return num + ten + ten_2
    return add_twice
  return add

closure_result = add_ten()
print(closure_result()(4))


# closures are just function inside a function with global vs local difference 

# nested functions , just encapsulating one function inside a function and returning the inner function


