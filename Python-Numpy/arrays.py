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


