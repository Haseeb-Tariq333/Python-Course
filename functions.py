def my_func(param1 = "Default"):
    """_summary_

    Args:
        param1 (str, optional): _description_. Defaults to "Default".
    """
    
    print(f"My first Python function!{param1}")
    
    
my_func()

### RETURN FUNCTIONALITY ###
def hello():
    return "hello"
result = hello()
print(result)


###############################

def addition(num1, num2):
    if type(num1) == type(num2) == type(10):
        return num1*num2
    else:
        print("Sorry give me an integer")
result = addition(2,3)
print(result)    

## FILTERING ##
my_list  = [1,2,3,4,5,6,7,8,9]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool,my_list)
print(list(evens))