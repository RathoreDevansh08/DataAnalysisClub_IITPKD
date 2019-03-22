#This is the first exercise of the python session, it will check your python syntax skills.....
#Complete the functions below by appropriately writing the code between the comments and the return statement

#Basic python

def sumTwoNums(a,b):
	#This is an example of how you should be completing the functions below
	#You should write the code between the comments and return statement and finally return appropriate variable
	#Start code----
	sumVal = a + b
	#End code------
	return sumVal

def subTwoNums(a, b):
	#Subtract b from a and return the value
	return

def integerDiv(a, b):
	#Divide a by b using integer division
	return

def fractionalPart(a):
	#Return the fractional part of a floating point number
	return

#Conditional statements & Loops

def findMax(a, b, c):
	#Return the max of a, b and c
	return

def checkPrime(n):
	#Return 1 if prime else return 0
	return

#List data structure

def maxArray(a):
	#Return the maximum element in the array
	return

def reverseArray(a):
	#Return the array in reversed order
	return

#Dictionary data structure

def returnKey(parameter, key):
	#return the element corresponding to the key 'key'
	return

def returnDict(keys, values):
	#Given two lists, create and return a dictionary corresponding to the keys and values
	return

#Tuple data structure

def returnSubTuple(a, i, j):
	#return the subtuple starting from ith element to jth element
	return

def listToTuple(a):
	#Given a list, create a tuple version of it and return it
	return

#Strings

def appendStr(a, b):
	#Append a and b and return the result
	return

def lenDiff(a, b):
	#Return the absolute value of the difference between the lengths of a and b
	return
#------------------------------------------------------

#Make a function to calculate the factorial of n with the name 'factorial' which takes the input 'n' and returns factorial.

####Write your code here#####


#############################

#------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------------

#Don't modify the content below-------


print("------------------Python Exersice 1-----------------")
print("Your answers will be shown below.....")

print("0- Example functions " + str(sumTwoNums(3,5)))
print("1- "+str(subTwoNums(24,-30)))
print("2- "+str(integerDiv(10,3)))
print("3- "+str(fractionalPart(3.14)))
print("4- "+str(fractionalPart(2)))
print("5- "+str(findMax(3,-123,540)))
print("6- "+str(checkPrime(23)))
print("7- "+str(checkPrime(40)))
print("8- "+str(maxArray([3,123,41,-55,134,403,1,2])))
print("9- "+str(reverseArray([7,6,5,4,3,2,1,0])))
print("10- "+str(returnKey({'a':40,'sith':500,'jedi':250},'jedi')))
print("11- "+str(returnDict(['a','b','c'],[1,2,3])))
print("12- "+str(returnSubTuple((1,2,3,4,5,6,7,8),2,4)))
print("13- "+str(listToTuple([1,2,3,4,5,6,7,8,9,0])))
print("14- "+str(type(listToTuple([1,2,3]))))
print("15- "+str(appendStr("Yo ","People")))
print("16- "+str(lenDiff("Yo","People")))

for i in range(2,8):
	print(str(i + 15) + "- " + str(factorial(i)))
