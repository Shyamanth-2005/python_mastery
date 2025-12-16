# Day 2: 30 Days of python  programming 
import math
first_name = "shyamanth"
last_name = "reddy"
full_name = "shyamanth reddy"
country = "India"
city = "Chennai"
age = 21
year = 2025
is_married = False
is_true = False
is_light_on = True
user_profile  = {
  "first_name":first_name,
  "last_name":last_name,
  "full_name":full_name,
  "age":age
}

print(type(user_profile))
print(len(first_name))
print(len(first_name) > len(last_name))
num_one = 5
num_two = 4
total = num_one+ num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division  = math.floor(num_one/num_two)

radius = 30
area_of_circle = 3.14 * radius**2
circumference_of_circle = 3.14 * 2 * radius
user_radius = int(input("Enter the radius of the circle: "))
user_area_of_circle = 3.14 * user_radius**2


first_name = input("Enter your first name: ")
last_name = input("Enter your last_name: ")

print(help('keywords'))