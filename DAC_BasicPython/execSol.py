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
	return a - b

def integerDiv(a, b):
	#Divide a by b using integer division
	return a // b

def fractionalPart(a):
	#Return the fractional part of a floating point number
	return a - int(a)

#Conditional statements & Loops

def findMax(a, b, c):
	#Return the max of a, b and c
	maxVal = a
	if b > a:
		maxVal = b
	if c > maxVal:
		maxVal = c
	return maxVal

def checkPrime(n):
	#Return 1 if prime else return 0
	for i in range(2,int((n)**(1/2))):
		if n%2 == 0:
			return 0
	return 1

#List data structure

def maxArray(a):
	#Return the maximum element in the array
	maxVal = a[0]
	for i in range(2,len(a)):
		if maxVal < a[i]:
			maxVal = a[i]
	return maxVal

def reverseArray(a):
	#Return the array in reversed order
	n = len(a)
	for i in range(int(n/2)):
		temp = a[n-i-1]
		a[n-i-1] = a[i]
		a[i] = temp
	return a

#Dictionary data structure

def returnKey(parameter, key):
	#return the element corresponding to the key 'key'
	return parameter[key]

def returnDict(keys, values):
	#Given two lists, create and return a dictionary corresponding to the keys and values
	parameters = {}
	for i in range(len(keys)):
		parameters[keys[i]] = values[i]
	return parameters

#Tuple data structure

def returnSubTuple(a, i, j):
	#return the subtuple starting from ith element to jth element
	return a[i:j]

def listToTuple(a):
	#Given a list, create a tuple version of it and return it
	return tuple(a)

#Strings

def appendStr(a, b):
	#Append a and b and return the result
	return a+b

def lenDiff(a, b):
	#Return the absolute value of the difference between the lengths of a and b
	return abs(len(a) - len(b))
#------------------------------------------------------

#Make a function to calculate the factorial of n with the name 'factorial' which takes the input 'n' and returns factorial.

####Write your code here#####

def factorial(n):
	factVal = 1
	for i in range(2,n):
		factVal = factVal*i

	return factVal
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
