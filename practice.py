class MyClass:
    i = 12345
    def f(self):     
        return 'hello world'
x = MyClass() 
print (x.i)
print (x.f())


def even(arr):
    n=10
    for i in range(n):
        if arr[i]%2 == 0:
            print(arr[i])

my_list = [1,2,3,4,5,6,7,8,9,10]
even(my_list)


my_dictionary = {"Haseeb": 456, "Habib": 234, "Usman": 123}

n = 3
for key, value in my_dictionary.items():
    print({key}, {value})
