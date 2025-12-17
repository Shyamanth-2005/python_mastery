"""
syntax
[i for i in iterable if expression]
"""

language  = "Python"

lst = list(language)


print(type(lst))
print(lst)


# sencond way

lst = [char for char in language]
print(type(lst))



# generating the numbers

numbers = [num for num in range(1,11)]
print(numbers)


# generating the sqaure of the numbers

squares  = [num * num for num in numbers]
print(squares)

# generating the number and it's sqaure in tuple

num_squar = [(num,num*num) for num in numbers]

print(num_squar)

# generating the odd numbers by putting condtion

odd_num = [num for num in range(21) if num % 2 != 0]
print(odd_num)


numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]

positive_even_num = [num for num in numbers if num % 2 == 0 and num > 0]
print(positive_even_num)