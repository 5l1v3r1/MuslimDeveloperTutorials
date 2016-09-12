#!/usr/bin/python

#This function adds two numbers

def manu(x,y,m="+"):
	if m == "*":
		return x * y
	elif m == "+":
		return x + y
	elif m == "-":
		return x - y
	elif m == "/":
		return x / y
	else:
		return "Unkown"

xstr = raw_input("Please enter the first number: ")
x = float(xstr)

ystr = raw_input("Please enter the second number: ")
y = float(ystr)

m = raw_input("Please enter your wanted operator: ")

result = manu(x=x, y=y, m=m)
print result


