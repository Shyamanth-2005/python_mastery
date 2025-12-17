list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

lst =[ k for i in list_of_lists for j in i for k in j ]

print(lst)

lst = [(num,num**0,num**1,num**2,num**3,num**4,num**5) for num in range(11)]

print(lst)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]


countries = [[country.upper(),country[:3].upper(),city.upper()] for entry in countries for country,city in entry]

print(countries)



y_linear_intercept = lambda x,m,c : m*x + c

y = y_linear_intercept(23,2,32)

print(y)