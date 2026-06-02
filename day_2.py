#CONDITIONAL STATEMENTS========================================
#if , elif, else
#age = 14
#if age >= 18:
#    print("you can vote")
#else:
#    print("you cannot vote at this age")


# ELIF condition==============

#color = input("enter color of traffic light:")
#if color == "red":
#    print("stop")
#elif color == "yellow":
#    print("look")
#elif color == "green":
#    print("go")
#else:
#    print("wrong color entered")

#age = int(input("enter your age:"))
#if age < 13:
#    print("child")
#elif age >= 13 and age < 18:
#    print("teenager")
#elif age > 18:
#    print("adult")

#username = input("enter username")
#password = input("enter password")
#if(username == "admin" and password == "pass"):
#    print("login success")
#else:
#    print("incorrect credentials")

#num = int(input("enter a num:"))
#if( num % 2 == 0):
#    print("even")
#else:
#    print("odd")

#NESTING================================
#condition inside a condition

#username = input("enter username")
#password = input("enter password")
#
#if(username == "admin" and password == "pass"):
#    print("success")
#else:
#    if(username != "admin"):
#        print("wrong username")
#    else:
#        print("wrong password")


# MATCH CASE IN CONDITIONAL STATEMENT===============================
#alternate for if else elif

#color = input("enter color of traffic light:")
#
#match color:
#    case "green":
#        print("Go")
#    case "yellow":
#        print("look")
#    case "red":
#        print("stop")
#    case _:
#        print("wrong color")

# LOOPS======================================================

# infinite while loop
#while 3 > 1:
#    print("hello world")

#i = 0 #iterator or counter
#while i < 5:
#    print(i)
#    i += 1

#multiplication table of any number
#i = 1
#num = int(input("enter num: "))
#while i <=10:
#    print(num * i)
#    i += 1


# BREAK AND CONTINUE KEYWORDS=================================================

#break----------------
#i = 1
# num = int(input("enter num: "))
#while i <=10:
#    if (i % 6 == 0):
#        break
#    print(i)
#    i += 1

#continue--------------
#i = 0
#while i < 10:
#    i += 1
#    if (i % 2 == 0):
#        continue
#    print(i)


# FOR LOOPS=========================================================
#using for sequencial traversal

string = "hello"

#in => membership operator (check presence)

#for var in string:
#    print(var)

#for i in range(5):
#    print(i+1)

# count the number of i's => 5
# word = "artificial intelligence"
# occurance = 0
# for i in word:
#     if(i == "i"):
#         occurance += 1
# print(occurance)

# print vowel count of a given string => 5
# word = "artificial"
# ans = 0
# for i in word:
#     if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
#         ans += 1
# print(ans)

# RANGE FUCNTION================================================
# generate sequence of numbers
# range(start, stop, step) =====> stop value is compulsory
# default start = 1
# default stop = +1
# range(5) ---->  0,1,2,3,4
# range(1,6) ----> 1,2,3,4,5
# range(1, 10, 2) -----> 1,3,,5,7,9

# for i in range(2,11, 2):
#     print(i)

# print sum of first n natural numbers
# num = int(input("enter number :"))
# sum = 0
# for i in range(1,num+1):
#     sum += i
# print(sum)

# FUNCTIONS IN PYTHON=======================
#blocks of statements that performs a specific task
#reusable components of code

# def hello():
#     print("hello")

# hello()

# def sum(a,b): #a and b are parameters
#     s = a+b
#     return s

# print(sum(2,5)) # 2 and 5 are arguments

# def avg(a,b,c):
#     val = (a+b+c) / 3
#     return val
# print(avg(1,2,3))

# def sum(a,b=1): #a and b are parameters
#     s = a+b
#     return s
# print(sum(4))

# BUILT IN FUCNTIONS (range, type, input, print)===============================
# USER DEFINED FUCNTIONS=======================================================

# LAMBDA FUNCTIONS 
#small anonymous fucntions

# sum = lambda a,b: (a+b)/2
# print(sum(4,5))

# WAP to print factorial of any number n
def calc_factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact*i
    return fact

print(calc_factorial(5))
