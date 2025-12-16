multiline_string = '''I am shyamanth , currently pursuing my 
bacholors at Vellore Institute of Technology , Chennai in the department of
Computer Science and Engineering with Specialization in Artifical Intelligence and
Machine Learning
'''
print(multiline_string)
a = 24
b = 3

print("{} /{} = {:.2f}".format(a,b,a/b))

language = "java"
a,b,c,d = language

print(a,b,c,d)

web_stack = ['HTML','CSS','JAVASCRIPT']

result = ' '.join(web_stack)
print(f"I am learning {result}")

challenge = "I am learnig python and i want to master the language python"

print(challenge.replace("python","java"))

name = "Shyamanth"
age = 21
country = "India"
city = "Chennai"
print("Name\t\tAge\tCountry\tCity")
print("{}\t{}\t{}\t{}".format(name,age,country,city))
check = "thiry_days_of_python"
print(check.isidentifier())