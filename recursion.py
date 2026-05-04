def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))

## Fibonacci Sequence ##
# 0 1 1 2 3 5 8 13 21
#f(n) = f(n-1) + f(n-2)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n-2)
terms = 10 ## number of terms wanted
for i in range(terms):
    print(fibonacci(i), end=" ")
    

## Binary Search using recursion

def binary_search(arr, target, high, low):
    if low == high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif target < mid:
        return binary_search(arr, target, mid -1, low)
    elif target > mid:
        return binary_search(arr, target, high, mid+1)

my_list = [1,3,5,7,9,11,13,17,23,29,37]
target_val = 7
result = binary_search(my_list, target_val, len(my_list)-1, my_list[0])
print(result)
