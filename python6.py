"""
#
#part: python Function
#
"""

def my_function():
    print("Hello World 3")
    print("Hello World 4")

my_function()
my_function()

#parmeter
def my_name(fname):
    print("My name is ",fname)

my_name("Anya")

def my_name(fname,Lname):
    print("My name is ",fname,Lname)

my_name("Anya","Roger")
my_name(Lname="Roger",fname="Anya")

def my_name3(Lname= "Roger"):
    print("My last name is ", Lname)

my_name3()
my_name3("Paul")

def my_fruits(frits):
    for fruit in frits:
        print(frits)

fruits = ["Apple","Banana","Coconut"]
my_fruits(fruits)

def red_potion(hp):
    return hp + 50

print("HP:",red_potion(100))
print("HP:",red_potion(70))

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

fruits_with_a = [fruit for fruit in fruits if 'a' in fruit]

print(fruits_with_a)
