#------SETS------
# It is an unordered list 

x = set()
x.add(1)
x.add(10)
x.add(2)
x.add(4)
x.add(4)
x.add(4)
x.add(4.1)
x.add(199)
x.add(2344)

print(x)
# It only takes unique elements, there were three 4's but it printed it only once


converted = set([1,1,1,1,2,2,2,2,3,3,3])
print(converted)

#we can convert a list into set