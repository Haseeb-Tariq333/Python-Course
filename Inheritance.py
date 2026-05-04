class Employee:
    def __init__(self, name, id):
        self.name = name 
        self.id = id
    def show_details(self):
        print(f"The name of employee id: {self.id} is {self.name}")
a = Employee("Haseeb", "300")
a.show_details()

## Programmer class extends the employee class and has all the methods of employee class ##
class Programmer(Employee):
    def language(self):
        print(f"The employee {self.name} with id {self.id} codes python")
b = Programmer("Ali", "400")
b.language()
## This is just a basic demonstration of how inheritance works ##

## Access Modifiers ##
class People:
    def __init__(self):
        self.name = "Haseeb"
a = People()
print(a.name)
##  We see that this block of code were correctly and the name variable was accessed from the class directly
##  so this type is called public

class Student:
    def __init__(self):
        self.__name = "Haseeb" ## In self.__name the "2 undersocres" indicate that this variable is private 
a = Student()
# print(a.__name)   ## This is not going to work because the name cant be accessed directly 
# Private variales can be accessed indirectly by usig the following methos
print(a._Student__name) ## This is called "name mangling"

