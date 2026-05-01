mylist = [1,2,'uhfiu',33,'fd']
print(mylist)

mylist[0] = 3
print(mylist)

mylist.append("New Item")
print(mylist)

mylist.append(["New1","New2", "New3"])
print(mylist)

listtwo = [1,2,3,4]
mylist.extend(listtwo)
print(mylist)

item = mylist.pop(3)
print(mylist)
print(item)

mylist.reverse()
print(mylist)

list3 = [2,4,2,1,6,2,1]
list3.sort()
print(list3)
print("/n")
print("-------------------")
print("-------------------")
print("-------------------")
print("-------------------")


list4 = [1,2,3,['x','y','z']]
print(list4 [3][1])