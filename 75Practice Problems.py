import math
## Question 1 ##
print("Question 1")
print("Hello World")

## Question 2 ##
print("Question 2")
name = "Haseeb"
print("Your name = ", name)

## Question 3 ##
print("Question 3")
message = "How are you"
print(message)

##Question 4 ##
print("Question 4")
a = input("What is your name: ")
print(a)

## Question 5 ##
print("Question 5")
b = float(input("Emter value 1 : "))
c = float(input("Enter value 2 : "))
print("Addition = ", b+c )
print("Multiplication : ", b*c )
print("Division : ", b/c)
print("Subtraction : ", b-c)

## Question 6 ##
print("Question 6")
d = True
print(d)

## Question 7 ##
print("Question 7")
my_string = "12345"
convert_to_int = int(my_string)
print("String converted to int is : ", convert_to_int)

## Question 8 ##
print("Question 8")
e = float(input("Enter the number : "))
if e>0:
    print("Number is postive")
elif e<0:
    print("Number is negative")
else:
    print("Number is zero")

## Question 9 ##
print("Question 9")
f = float(input("Enter the number : "))
if f%2==0:
    print("Number is positive")
else:
    print("Number is negative")

## Question 10 ##
print("Question 10")
g = float(input("Enter the number : "))
h = float(input("Enter the number : "))
i = float(input("Enter the number : "))
largest  = max(g,h,i)
print("Largest = ", largest)

## Question 11 ##
print("Question 11")
year = int(input("Enter the year : "))
if (year%2==0 and year%100 != 0 ) or (year%400 == 0):
    print("It is a leap year")
else:
    print("It is not a leap year")

## Question 12 ##
print("Question 12")
def isPrime(j):
    Prime = True
    for i in range(3,j):
        if j%i==0:
            Prime = False
    if Prime == True:
        print("Number is prime")
    else:
        print("Number is nnot prime")
isPrime(101)

## Question 13 ##
print("Question 13")
my_str = "racecar"
rev_string = reversed(my_str)
if list(my_str) == list(rev_string):
    print("It is palindrome")
else:
    print("It is not palindrome")

## Question 14 ##
print("Question 14")
k = float(input("Enter the number : "))
l = float(input("Enter the number : "))
largest = max(k,l)
smallest = min(k,l)
print("Largest is : ", largest)
print("Smallest : ", smallest)

## Question 15 ##
print("Question 15")
vowels = ['a','e','i','o','u','A','E','I','O','U']
char = input("Enter char = ")
if  char in vowels:
    print("Vowel")
else:
    print("Constant")

## Question 16 ##
print("Question 16")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b**2 - 4*a*c

if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    
    print(f"The roots are {root1} and {root2}")
else:
    print("The roots are complex/imaginary.")

## Question 17 ##
print("Question 17")
number = 1
while number<=10:
    print(number)
    number += 1

## Question 18 ##
print("Question 18")
for number in range(2,21,2):
    print(number)

## Question 19 ##
print("Question 19")
def fibonaaci(n):
    if n <= 1:
        return n 
    else:
        return fibonaaci(n-1) + fibonaaci(n-2)
n = int(input("Enter c: "))
for i in range(n):
    print(fibonaaci(i), end=" ")
  
## Question 20 ##
print("Question 20")
def factorial(n):
    if n<=1:
        return n
    else:
        return n*factorial(n-1)
fact = int(input("Enter the number you want to find the factorial of: "))
factorial(fact)
  
## Question 21 ##
print("Question 21")
num = int(input("Enter the number whose multiplication table you want : "))
for i in range(11):
    print(f"{num} x {i} = {num*i}" )
    
## Question 22 ##
print("Question 22")
num = int(input("Enter number to find the sum of natural numbers upto this number: "))
i = 1
for i in range(num+1):
    sum = sum + i
print(sum)

## Question 23 ##
print("Question 23")
num = int(input("Enter the number you want to reverse: "))
reversed_num = 0
while n>0:
    last_digit = num % 10
    reversed_num = (reversed_num*10) + last_digit
    num = num // 10
print("The reversed number is = ", reversed_num)
    
   
 ## Question 24 ##
print("Question 24")
fruits = ["apple", "banana", "mangoe", "orange"]
print(fruits)   

 ## Question 25 ##
print("Question 25")
fruits = ["apple", "banana", "mangoe", "orange"]
print(fruits[0])
print(fruits[1])
print(fruits[-1])

 ## Question 26 ##
print("Question 26")
fruits = ["apple", "banana", "mangoe", "orange"]
fruits.append("Beetroot")

 ## Question 27 ##
print("Question 27")
nums_list = [10,100,40,5,78,56]
nums_list.sort()
print(nums_list)

 ## Question 28 ##
print("Question 28")
fruits = ["apple", "banana", "mangoe", "orange"]
if "banana" in fruits:
    print("Banana is in fruits")
else:
    print("Not in fruits")

 ## Question 29 ##
print("Question 29")
def add(a, b):
    sum = a+b
    print("The sum of the two numbers is ", sum)
a = int(input("Enter number a : "))
b = int(input("Enter number b : "))

add(a, b)

 ## Question 30 ##
print("Question 30")
def square(a):
    sqr = a**2
    print("The square of the number is ", sqr)
a = int(input("Enter number a : "))

square(a)

 ## Question 31 ##
print("Question 31")
def is_even_or_odd(number): 
    if number % 2 == 0: 
        return "Even" 
    else: 
        return "Odd" 
result = is_even_or_odd(7) 
print("Number is:", result) 

 ## Question 32 ##
print("Question 32")
def rectangle_area(length, width): 
    return length* width 
result = rectangle_area(5, 4) 
print("Rectangle Area:", result) 


 ## Question 33 ##
print("Question 33")
def convert_to_farenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit
celsius = float(input("Enter the temp in celsius: "))
print("Temperature in Fareheit is: ", convert_to_farenheit(celsius))


 ## Question 34 ##
print("Question 34")
def gcd(a,b):
    result = math.gcd(a, b)
    print(result)
a = int(input("Enter number a : "))
b = int(input("Enter number b : "))
gcd(a,b)



 ## Question 27 ##
print("Question 35")

 ## Question 27 ##
print("Question 36")

 ## Question 27 ##
print("Question 37")

 ## Question 27 ##
print("Question 38")

 ## Question 27 ##
print("Question 39")

 ## Question 27 ##
print("Question 40")

 ## Question 27 ##
print("Question 41")
