# OOPs===================================
# matching real world objects with code

# CLASSES AND OBJECTS
# class is a blueprint of an object
# class is creaetd once, class doesn't take much space
# object is an instance of class

# syntax
# class Student:
#     subject = "Python"
#     college = "ABC"
#     year = "4th year"
    
#     def fucntion():
        
    
# stud1 = Student()
# stud2 = Student()
# print(stud1.subject, stud1.college, stud1.year)
# print(stud2)

#CLASSES STORES BLUEPRINT AND ATTRIBUTES==========================
# blueprint have attributes and methods

#CONSTRUCTOR IN CLASSES=========================================
# _init_ method 
# used to initialise the object
# called everytime when obejct is created
# it called automatically

# def __init__(self): 
# self parameter stores the current instance of class
# stores a reference to the current object
# compulsory parameter
    
# class Student:
#     def __init__(self): #default
#         print("constructor")
#     def __init__(self, name, cgpa): #parameterized
#         self.name = name
#         self.cgpa = cgpa
    
#     def get_cgpa(self):
#         return self.cgpa
   
# stud1 = Student("rahul", 8.9)
# print(stud1.get_cgpa())

#Types of constructors 
# default and parameterized
# default = 1 parameter 
# parameterized = parameter other than self
# python allows one init constructor only, 

#ATTRIBUTES ===============================================
# classes and instance 
# class attributes belongs to classes #common
# instance attributes belongs to objects #unique

# instance attribute have high priority
# class Student:
#     college_name = "ABC" #collene_name is class attribute
#     Pi = 3.1
    
#     def __init__(self,name,cgpa):
#         self.name = name #instance attribute
#         self.cgpa = cgpa #instance attribute
#         self.Pi = 3.14

# stud1 = Student("rahul", 9)
# print(stud1.Pi)

#TYPES OF METHODS IN CLASSESS====================================
# instance, class, static 

#instance method
# self
class Laptop:
    storage_type = "ssd"
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage
        
    #instance method  (first parameter is self)
    #they can access the class and instance btoh attributes
    #for ex, storage_tyep is class attribue
    def get_info(self):
        print(f"Laptop has {self.ram} RAM, {self.storage} storage and {self.storage_type}")
        
    #class method (first attribute is cls)
    #tehy access only class attribues not instance attributes
    #can use decorators (@classmethod)
    @classmethod
    def get_storage_type(cls):
        print(f"storage type : {cls.storage_type}")
        
        
    #static method 
    #no compulsory parameter
    #cant access instance and class attr
    #decorator = @staticmethod
    @staticmethod
    def discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"Final price : {final_price}")

l1 = Laptop(16, 512)
l2 = Laptop(8, 256)
# Laptop.get_storage_type()
# l1.discount(40000, 10)

class Product:
    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1
        
    def get_info(self):
        print(f"price of the {self.name} is Rs.{self.price}")
    
    @classmethod
    def get_count(cls):
        print(f"Total products are: {cls.count}")
    
    @staticmethod
    def discount(price, discount):
        final_price = price - (price * discount /100)
        print(f"Discount Price = {final_price}")
p1 = Product("mobile", 10000)
p2 = Product("laptop", 50000)
p3 = Product("headphone", 8000)
# p1.get_info()
# Product.get_count()
# p1.discount(40000, 10)


#OOPS Pillars==============================================
# 1. Encapsulation
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphysm

#Encapsulation======================
# wrapping data and functions in single unit
# data hiding
# public attr - access inside class & methods (everywhere access)
# protechted attr - acces in class and sub class
# private attr - access inside the class

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        # self._balance = balance  #protected attr
        self.__balance = balance  #private attr
    
    def get_balance(self): #getter
        return self.__balance
    
    def set_balance(self, newBalance):
        self.__balance = newBalance

acc1 = BankAccount("Rahul Kumar", 100000)
acc1.set_balance(2000000)
print(acc1.get_balance())


#Inheritance ============================================
#reusing attr and methods from parent or base class in its sub classes
# class Employee:
#     start_time = "10am"
#     end_time = "6pm"
    
#     def change_time(self, newEndTime):
#         self.end_time = newEndTime
        
# class Teacher(Employee):
#     def __init__(self,subject):
#         self.subject = subject

# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role = role

# tch1 = Teacher("Maths")
# tch1.change_time("5pm")
# a1 = AdminStaff("Manager")
# print(a1.role, tch1.start_time, tch1.end_time)

#Types of inheritance===============================

# 1st - Single level inheritance
# only parent and child level of classes

# 2nd  Multi level inheritance
# multiple classes

# class Employee:
#     start_time = "10am"
#     end_time = "6pm"
        
# class Teacher(Employee):
#     def __init__(self,subject):
#         self.subject = subject

# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role = role

# class Accountant(AdminStaff):
#     def __init__(self, salary, role):
#         super().__init__(role)
#         self.salary = salary

# ac1 = Accountant("250000", "CA")
# print(ac1.salary, ac1.role, ac1.start_time, ac1.end_time)

# 3rd - Multiple inheritance

class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, gpa):
        self.gpa = gpa
        
class TA(Teacher, Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name

ta1 = TA("15000", 9.3, "Khushi")
# print(ta1.name, ta1.gpa, ta1.salary)

# Abstraction========================================================
#hiding internal details and showing only essestial features
#abstract classes are blueprint for other classes we create
from abc import ABC, abstractmethod
class Animal:
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar!")
        
class Cow(Animal):
    def make_sound(self):
        print("Moo!")
l1 = Lion()
l1.make_sound()
m1 = Cow()
m1.make_sound()


#Polymorphism========================
#many forms
# 1t function  overriding = redifining parent class fucn in child class
#example

# class Employee:
#     def get_designation(self):
#         print("designation = Employee")

# class Teacher(Employee):
#     def get_designation(self):
#         print("designation = Teacher")

# t1 = Teacher()
# t1.get_designation()

#2nd duck typing
# if something walks like a duck and quack like a duck
# same fucntion exist in both classes, no matter if both classes are related or not

class Teacher():
    def get_designation(self):
        print("designation = Teacher")
        
class Accountant():
    def get_designation(self):
        print("designation = Accountant")
        
t1 = Teacher()
t1.get_designation()

a1 = Accountant()
a1.get_designation()







    






    
