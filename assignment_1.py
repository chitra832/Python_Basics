#1 Write a program that asks the user for their name and age,then prints a sentence like
#-----------> Hello Shradha, you are 21 years old!

#name = input("enter your name:")
#age = input("enter your age:")
#print("Hello " + name +',' + " you are " + age + " years old!")

#2 Take two numbers as input from the user and print their sum,difference,product,and quotient
#num1 = int(input("enter 1st num:"))
#num2 = int(input("enter 2nd num:"))
#
#sum = num1 + num2
#diff = num1 - num2
#product = num1 * num2
#quotient = num1 / num2
#print("Sum of " + str(num1) + " and " + str(num2) + " - " + str(sum))
#print("Difference of " + str(num1) + " and " + str(num2) + " - " + str(diff))
#print("Product of " + str(num1) + " and " + str(num2) + " - " + str(product))
#print("Quotient of " + str(num1) + " and " + str(num2) + " - " + str(quotient))

#3 Ask the user to enter 2 integers and a float, convert them all to float and print their average
#num1 = float(input("enter 1st integer num:"))
#num2 = float(input("enter 2nd integer num:"))
#num3 = float(input("enter a float num:"))
#
#avg = (num1 + num2 + num3) / 3
#print("Average of " + str(num1) + " , " + str(num2) + " , "  + str(num3) + " is " + str(avg))

#4 The user enters a string containing a number (e.g., "45" ). Convert it to:
#• an integer
#• a float
#• a string again
#Print all three values with their types
#num_str = input("enter a number (as string):")
#num_int = int(num_str)
#num_float = float(num_str)
#num_back_str = str(num_int)
#
## Print values with types
#print("Integer value:", num_int, "Type:", type(num_int))
#print("Float value:", num_float, "Type:", type(num_float))
#print("String value:", num_back_str, "Type:", type(num_back_str))

#5 Evaluate and print the result of the following expression:
#x = 10 + 3 * 2 ** 2
#Based on what you learnt in the lecture explain why the output is what it is. 
#x = 10 + 3 * 2 ** 2
#print(x)

#6 Write a program to swap values of two numbers entered by the user.
#a = input("enter 1st num:")
#b = input("enter 2nd num:")
#print("Before swapping:")
#print("a =", a)
#print("b =", b)
#c = a
#a = b
#b = c
#
#print("After swapping:")
#print("a =", a)
#print("b =", b)

#7 Ask the user for a temperature in Celsius (string input). Convert it to float,
#then calculate and print temperature in Fahrenheit.
#temp = float(input("enter temperature in Celsius:"))
#temp_in_fahrenheit = (temp * (9/5)) + 32
#print(temp_in_fahrenheit)

#8 Take the radius (r) as user input and print the area
#r = int(input("Enter radius:"))
#PI = 3.14
#area = PI * r**2
#print(area)

#9 Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and
#compute simple interest:
#p = float(input("Enter Principal:"))
#r = float(input("Enter rate:"))
#t = float(input("Enter time:"))
#SI = (p * r * t) / 100
#print(SI)

#10 Take a decimal number as input (like 45.78 ) and output its:
#• integer part - 45
#• fractional part - .78
num = float(input("Enter a number:"))
integer_part = int(num)
fractional_part = num - integer_part
print("integer part: ", integer_part)
print(f"Fractional part: {fractional_part:.2f}")

