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