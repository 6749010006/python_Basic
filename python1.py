"""
#
#part: python comment
#
"""
# this is a comment
# writting
# v = s/t
# v = ความเร็ว (m/s)
# s = ระยะทาง (m)
# t = ระยะเวลา (s)
print ("Hello World 1")

"""
# v = s/t
# v = ความเร็ว (m/s)
# s = ระยะทาง (m)
# t = ระยะเวลา (s)
print("Hello World 2")
"""
#
# Part : Python Variables 
#
""" ระยะทาง (m)
# t = ระยะเวลา (s)
"""
x = 5
y = "Hey Bro"
print(x,y)
x = str(3)
y = int(3)
z = float(3)
print(type(x),type(y),type(z))
"""
#
# Part : Python Names
#
"""
myvar = "John"
my_var = "John"
_My_var = "John"
myVar = "John"
MYVAR = "John"
MY_VAR = "John"
myvar2 = "John"
# 2myvar = "John"
# my-var = "John"
# my var = "John"

#camel case
myVariableName = "John"
# Pascal case
MyVariableName = "John"
# Snake Case
my_variable_name = "John"
"""
#
# Part : Python "String
#
"""
x = "Hey Bro"
print(x)

y = """1 Hey Bro
2 Hey Bro
3 Hey Bro 4 Hey Bro
5 Hey Bro"""
print(y)

x="Hey Bro"
print(x[2])
print(len(x))

print("Hey" in x) 
print("what sup" not in x)
print(x.upper())
print(x.lower())
print(x.replace("Bro","Sis"))
print(x.split(" "))
a = "Apple"
b = "Banana"
print( a+ " "+ b) 

price = 20
word = f"Price: {price:.2f}"
print(word)