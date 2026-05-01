###############
## PROBLEM 1 ##
###############

# Given the string 
s = 'django'
## Use indexing to print the following
print(s[0])  ## 'd'
print(s[-1]) ## 'o'
print(s[0:4])  ## 'djan'
print(s[1:4]) ## 'jan'
print(s[4:]) ## 'go'
print(s[::-1]) ## Reversed String


###############
## PROBLEM 2 ##
###############

## Reassign "hello" to be "goodbye" in the given list
l = [3,7,[1,4,'hello']]
l[2][2] = 'goodbye'  ## REASSIGNED
print(l)


###############
## PROBLEM 3 ##
###############

## Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple key': 'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])


###############
## PROBLEM 4 ##
###############

## Use a set to find the unique values in the given list

mylist = [1,1,1,1,2,2,2,2,3,3,3,3]
x = set(mylist)
print(x)


###############
## PROBLEM 5 ##
###############

##Your are given two variables

age = 4 
name = "Sammy"

#Use print formatting to print the following string
"Hello my dogs name is Sammy and he is 4 years old"

mystring = "Hello my dogs name is {} and he is {} years old".format(name,age )
print(mystring)


#########################################