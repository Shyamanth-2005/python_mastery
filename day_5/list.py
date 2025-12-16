country = ['India','China','USA','Russia','France','Austrailia','UK','Canada']

print(*country)

print(country[1:3])
country.append('South Korea')

country.insert(2,'Brazil')
print(country)
country.remove('China')
print(country)
country.pop()
country.pop(1)

del country[1]
del country[1:2]
# del country

# country.clear()
list_copy  = country.copy()
lst1 = [1,2,3]
lst2 = [-1,-2,-3]
lst3 = lst1 + lst2
print(lst3)
lst1.extend(lst2)
print(lst1)
lst1.reverse()
print(lst1)
lst1.sort()
lst1.sort(reverse=True)
print(sorted(lst1))

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end

full_stack.insert(full_stack.index('Node'),'python')
full_stack.insert(full_stack.index('Node'),'SQL')
print(full_stack)

country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first_country,second_country,third_country,*scandic = country
print(scandic)

absolute_difference  = abs(min(lst1)-max(lst1))
