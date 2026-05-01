### FOR LOOPS ###
#################

seq = [1,2,3,4,5]

for i in seq:
    if i<3:
        print(i)
        

## FOR LOOP IN DICTIONARIES ##

d = {"Sam": 1, "Dan": 3, "Ali":4}

for key, value in d.items():
    print(f"{key}  {value}")

## FOR LOOP IN TUPLE WITHIN A LIST ##

mypairs = [("Haseeb", "AI Engineer"), ("Ali", "Software Engineer"), ("Ahmed", "HR Manager")]

for name, role in mypairs:
    print(f"{name} works as a {role}")


### WHILE LOOPS ###
###################

i = 1
while i<5:
    print(f" i is {i}")
    i = i+1

### RANGE FUNCTIONS ###
#######################

a = range(5)
print(a)
b = list(range(0,5))
print(b)
c = list(range(0,20,2))
print(c)
print(c[4]) ### prints 8 

for item in range(10):
    print(f"The num is {item}")


### LIST COMPREHENSHION ###

## METHOD 1
x = [1,2,3,4,5]

out = []
for num in x:
    out.append(num**2)
print(out)


## METHOD 2 

y = [1,2,3,4,5]
out = [num**2 for num in y]
print(out)
    
