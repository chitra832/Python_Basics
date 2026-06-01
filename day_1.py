name = "chitra"
#print(type(name))


# Style guide
# exixting python fucntions and libraries use snake case
tot_price = 10 #snake case---------------------------
totPrice = 20 #camel case
TotPrice = 30 #pascal case

# WAP to calculate sum of 2 numbers
a = 10
b = 3
sum = a + b
#print(sum)

#Operators

#arithmetic (+, -,/, %, *, **)
#print(a-b)
#print(a/b)
#print(a%b) #modulo
#print(a*b) 
#print(a**b)

#Relational / Comparison ( <, >, <=, >=, ==, != )
# returns true or false 
#print(3 > 6)
#print(a != b)

#Assignment Operators
# ----> =, +=, -=, *=, /=, %=, **=
a += 5
#print(a)

#Logical Operators 
# NOT (reverse a value), AND, OR
#print(not (5 > 4)) #False
#print((5 > 2) and (2 > 1)) #True
#print((5 > 7) and (2 > 1)) #False
#print((5 > 7) or (2 > 1)) #True

# Practise question
x = 3
x += 5
#print(x) #8

#Operators Precedence (priority) BODMAS
#()
#**
#*, / , %
#+, -
#==, !=, >=, <=, <, <
#not
#and
#or

r = 3 * 5 + 2 # 17 or 21-------------- 17 
#print(r)

# Type conversion

#2 types of type conversions are there :
#
#type conversion (implict by python)
#ex: float + int then result will always come in float
#type casting (explicit by developer)
#ex: int() float() bool()

num = 5 + 10.2
num2 = int(5 + 10.3)
#print(num, type(num)) #float
#print(num2, type(num2)) #int

# USER INPUT

#v = input("enter value of v:")
#print(v)    

# WAP to calculate sum of 2 numbers by taking input from user for numbers
#val1 = int(input("Enter value for num 1:"))
#val2 = int(input("Enter value for num 2:"))
#summ = val1 + val2
#print(summ)


# Print Average of 2 numbers

#n = int(input("enter num 1:"))
#n2 = int(input("enter num 2:"))
#avg = (n + n2)/2
#print(avg)