# This is a one-line Python comment - code blocks are so useful!
"""This type of comment is used to document the purpose of functions and classes."""

# Remember values, not variables, have data types.
# A variable can be reassigned to contain a different data type.
#Values have data type but not the varaibles.
answer = 42
answer = "The answer is 42."
print(answer)


#Datatypes in python.
boolean = True
number = 1.1
string = "Strings can be declared with single or double quotes."
list = ["Lists can have", 1, 2, 3, 4, "or more types together!"]
tuple = ("Tuples", "can have", "more than", 2, "elements!")
dictionary = {'one': 1, 'two': 2, 'three': 3}
variable_with_zero_data = None

print ("Printed!")

#Conditionals in Python.
def hello_i_love_cake(cake):
    if cake == "delicious":
        return "Yes please!"
    elif cake == "okay":
        return "I'll have a small piece."
    else:
        return "No, thank you."

print(hello_i_love_cake("delicious"))

#Loops in Python.
#list of items
item = [1,21,2,3]
a = "APPLE"
#Iterate throught the list and print the item one by one.
for items in item:
    print(items)
for letter in a:
    print(letter)

values= [1,2,3]
total = 3
max_val = 5
i =0
while (total < max_val):
    total += values[i]
    i += 2
print(total)

# fucntions in python.
def divide(dividend, divisor):
    quotient = dividend / divisor
    remainder = dividend % divisor
    return quotient, remainder

def calculate_stuff(x, y):
    (q, r) = divide(x,y)
    print (q, r)

#Classes in python3.
class Person:
    #This defines the attributes of the class Person.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1
        return self.age

p1 = Person("Sonam",28)
print("Next year he will be ",p1.birthday())
p1.birthday()

#Creating a class Robot in python.
#inheriting the Person class attributes and methods to Robot class.
class Robot(Person):
    #Creating a consturctor in python.
    def __init__(self,name,color,select,age):
        #set this object name to givenName.
        self.name = name
        self.color = color
        self.select = select
        self.age = age

    #When a function or method is inside a class you need to pass argument self.
    def intro(self):
        print("My name is " + self.name) # Self will define or point out to that object.
        print("My status " + self.select)
        print("My age ", self.age)

#Creating an object in python.
r1 = Robot("Tom","red","Selected",30)
r1.birthday()
# #Here self is pointing out to the r1 object name attribute value.
# r1.name = "Hello"
# r1.color = "Green"
# r1.select = "Selected"

#Accessing the methods defined inside the Robot class.
r1.intro()

list = [1,2,3]

a = 10
list.append(a)
print(list)


class Classy:
    def __init__(self):
        self.items = []

    def addItem(self,item_name):
        self.item_name = item_name
        self.items.append(self.item_name)
        print(self.items)

r1 = Classy()
r1.addItem("Bow")
r1.addItem("Howl")
