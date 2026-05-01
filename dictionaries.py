#dictionaries  KEY VALUE PAIRS

my_stuff = {"key1": 123, "key2": 456,}
print(my_stuff['key1'])

#nested
my_stuff = {"key1": 123, "key2": 456, "key3": {"key4": 789, "key5":"abc"}}
print(my_stuff['key3']['key4'])

#array inside dictionary
my_stuff = {"key1": 123, "key2": 456, "key3": {"key4": 789, "key5":"abc", "key6":[1,2,'haseeb']}}
print(my_stuff['key3']['key6'][2])

# In upper case using .upper() function 
my_stuff = {"key1": 123, "key2": 456, "key3": {"key4": 789, "key5":"abc", "key6":[1,2,'haseeb']}}
print(my_stuff['key3']['key6'][2].upper())

#Reassignment and adding mew key
my_stuff = {"lunch":"Pizza", "bfast": "eggs"}
my_stuff["lunch"] = "burger"
my_stuff["dinner"] = "pasta"
print(my_stuff["lunch"])
print(my_stuff["dinner"])