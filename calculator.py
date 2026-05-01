import math
## DISPLAY MENU ##
def menu():
        print("Choose Your Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Division")
        print("4. Multiplication")
        print("5. Factorial")
        print("6. Power")
        print("7. Natural Log (ln)")
        print("8. Log base 10")
        print("9. Exit")
## ADDITION OPERATOR       
def addition():      
            print("Enter numbers for addition")
            x = float(input("x : "))
            y = float(input("y : "))
            add = x+y
            print("Answer = ", add )
## SUBTRACTION OPERATOR           
def subtraction():       
            print("Enter numbers for subtraction")
            x = float(input("x : "))
            y = float(input("y : "))
            sub = x-y
            print("Answer = ", sub )
## DIVISION OPERATOR
def division():       
            print("Enter numbers for division")
            x = float(input("x : "))
            y = float(input("y : "))
            div = x/y
            print("Answer : ", div)
## MULTIPLICATION OPERATOR
def multiplication():
            print("Enter numbers for multiplication")
            x = float(input("x : "))
            y = float(input("y : "))
            mul = x*y
            print("Answer : ", mul)
## FACTORIAL
def factorial():
            print("Enter the number for its factorial")
            x = (input("x : "))
            fact = 1
            while x > 0:
                fact *= x
                x -= 1
            print("Answer = ", fact)
## POWER           
def power():
            print("Enter number and its power to find the answer") 
            x = float(input("x : "))    
            y = float(input("its power : "))
            power = x**y
            print("Answer : ", power)
## NATURAL LOG (LN)
def natural_log():
            print("Enter number to find its natural log")
            x = float(input("x : ")) 
            ln = math.log(x)
            print("Answer : ", ln)
## LOG BASE 10
def log_base10():
            print("Enter the number to find its log base 10")
            x = float(input("x : "))
            log = math.log10(x)
            print("Answer : ", log)
    
## EXIT 
def exit():
            print("Exiting the program...")
            print("Goodbye👋🏻")

    
def main():
    while True:
        menu()
        choice = int(input("Enter your choice (1-7): "))
        if choice == 1:
            addition()
        elif choice == 2:
            subtraction()
        elif choice == 3:
            division()
        elif choice == 4:
            multiplication()
        elif choice == 5:
            factorial()
        elif choice == 6:
            power()
        elif choice == 7:
            natural_log()
        elif choice == 8:
            log_base10()
        elif choice == 9:
            exit()
            break
        else:            
            print("Enter a correct choice")
main()

    
    
    
