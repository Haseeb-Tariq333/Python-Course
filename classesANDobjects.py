## Basic class and object demonstration ##
class Person:
    name = "Haseeb Tariq"
    age = 19
    occupation = "AI engineer"
    
    def info(self):
        print(f"{self.name} is {self.age} years old")
    
a = Person()
a.name = "Ali"
a.age = 25

b = Person()
b.name = "Daniyal"
b.age = 23

a.info()
b.info()


## Constructors ##
class Car:
    def __init__(self, t, m ):
        self.type = t
        self.model = m
        print(f"This is a {self.type} car model {self.model}")

a = Car("Hatchback", "2020")
b = Car("Sedan", "2025")     ## As you can see Constructors are making more organized and easy to read code ##


## Practice ##
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x*self.y
a = Shape(10, 2)
print(a.area())