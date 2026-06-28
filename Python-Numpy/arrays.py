import numpy as np
arr = np.array([1,2,3,4])
print(arr)

a = np.zeros(5)
print(a)

b = np.ones(10)
print(b)

c = np.arange(0,10)
print(c)

d = np.array([[8.0,7.0,9.0],[6.0,5.0,4.0]])
print(d)

## Get Dimensions ##
e = d.ndim
print(e)

## Get Shape ## rows and columns
e = d.shape
print(e)

## Get Size ##
e = arr.size
print(e)

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
## Get a specefic element from array (r, c)
print(a[1, 5])

## Get a specefic row 
print(a[0, : ])

## Get a specefic column
print(a[:,2])

## Getting a little fancy (startindex:endindex:stepsize)
print(a[0, 1:6:2])

## Reassigning values
a[1, 5] = 20
print(a) ## Vlue changed to 20 from 13
a[:,2] = [1,2]
print(a)


## 3-Dimensional ##
h = np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
    ])
print(h)

##  Get a specefic value (block, row, column)
print(h[1,0,2])
print(h[1, : , 2]) 
h[1, : , 2] = [1,2]
print(h)

print(h[:, 1 , :]) 

## Initializing different types of array ##
## All zeros ##
a = np.zeros(5)
print(a)
a = np.zeros((2,3))
print(a)
a= np.zeros(((2,3,3)))
print(a)

## All 1s matrix ##
b = np.ones((2,3))
print(b)

## Any other number ##
c = np.full((2,3), 77)
print(c)

## Random decimal numbers ##
d = np.random.rand(4,2)
print(d)

## Random integer numbers ##
e = np.random.randint(7, size=(3,2))
print(e)

## Repeat an array ##
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis = 0)
print(r1)

print("PRACTICE QUESTION")

output = np.ones([5,5])
print(output)

z = np.zeros([3,3])
print(z)
z[1,1] = 9
print(z)

output[1:4,1:4] = z
print(output)


## MATHEMATICS ##
print("MATHEMATICS")

a = np.array([1,2,3,4])
print(a+2)
print(a*2)
print(a-2)
print(a/2)
print(a**2)
print(np.sin(a))



b = np.array([5,6,7,8])
print(a+b)


## Linear Algebra ##
print("LINEAR ALGEBRA")
a = np.ones((2,3))
b = np.full((3,2), 2)
print(np.matmul(a,b))
## Finding Determinant ##
print("DETERMINANT")
c = np.identity(3)
print(np.linalg.det(c))



## Statistics ## 
print("STATISTICS")
stats = np.array([[1,2,3],[4,5,6]])
print(np.min(stats))
print(np.max(stats))
print(np.sum(stats))

print("REORGANIZING ARRAYS")
before = np.array([[1,2,3,4],[5,6,7,8]])
after = before.reshape(8,1)
print(after)


## Vertical stacking ##
print("Vertical Stacking")
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1,v2,v1,v2]))

## Horizontal Stacking ##
print("Horizontal Stacking")
print(np.hstack([v1,v2,v1,v2]))

