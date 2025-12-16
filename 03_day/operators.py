age = 21

height = 174.5

com_num = 23+ 1j
print(type(com_num))

base = int(input("Enter your triangle's base length: "))
height = int(input("Enter your triangle's height: "))
area = 0.5 * base * height
print(f"Area of the trinagle is {area}.")

print("Table")


for i in range(1,6):
  print(f"{i} 1 {i*1} {i**2} {i**3} ")