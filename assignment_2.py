#1 Write a program that takes salary as input. Using conditional statements,
# calculate the tax rate based on these rules:
# • If salary < 30,000 → 5%
# • If salary is 30,000–70,000 → 15%
# • If salary > 70,000 → 25%

# salary = int(input("enter salary:"))
# tax_rate = 0
# if(salary < 30000):
#     tax_rate = (salary * 5)/100
# elif(salary >= 30000 and salary < 70000):
#     tax_rate =  (salary * 15)/100
# else:
#     tax_rate = (salary * 25)/100
# print("Tax rate is: ", tax_rate)

#2 Write a function that takes two integers a and b and prints all even
# numbers between them (inclusive).

# def print_even_range(a,b):
#     for num in range(a, b+1):
#         if(num % 2 == 0):
#             print(num)
# num1 = int(input("enter 1st num:"))
# num2 = int(input("enter 2nd num:"))
# print_even_range(num1, num2)


#3 Write a function that prints the digits of a number, n .
# For eg: n = 312 , there are 3 digits in it 3, 1 and 2 & we need to print them.

# def print_digits(n):
#     while n > 0:
#         digit = n % 10
#         print(digit, '----', n)
#         n = n // 10
# num = int(input("enter num:"))
# print_digits(num)

#4 Write a function to return the count the number of digits in a number, n .

# def count_number_of_digit(n):
#     count = 0 
#     while n > 0:
#         count += 1
#         n = n // 10
#     print(count)

# num = int(input("enter num:"))
# count_number_of_digit(num)

#5 Write a function to return the sum of digits of a number, n

# def calc_sum_of_digits(num):
#     total = 0
#     while num > 0:
#         digit = num % 10
#         total += digit
#         num = num // 10
#     print(total)
# num = int(input("enter num:"))
# calc_sum_of_digits(num)

#6 Write a program to print all numbers from 1 to 100 that are divisible by both 3
#and 5.

# for i in range(1, 100 ):
#     if(i % 3 == 0 and i % 5 == 0):
#         print(i)

#7 Design a program to continuously input a number from user & print if it is
#positive or negative until the user enters “Quit”.

# while True:
#     user_input = input("enter a num or type Quit to stop")
#     if(user_input == "Quit"):
#         break
    
#     num = int(user_input)
#     if(num > 0):
#         print("positive")
#     elif(num < 0):
#         print("negative")
#     else:
#         print("zero")


