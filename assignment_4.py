#1-------------------------------------
class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, new_balance):
        self.balance += new_balance
        print("Balance deposit successfully!")
    
    def withdraw(self, new_balance):
        self.balance -= new_balance
        print("Balance withdrawn successful")
    
    def check_balance(self):
        print(f"Current balance = {self.balance}")

a1 = BankAccount(123454321, "Khushi", 8000000)
# a1.deposit(4000)
# a1.withdraw(100)
# a1.check_balance()
# print(a1.owner_name, a1.balance)

#2-----------------------------------------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._reviews = []
        
    def count_reviews(self):
        review_count = len(self._reviews)
        print(f"Total Reviews = {review_count}")
        
    def add_review(self, newReview):
        self._reviews.append(newReview)
        print("Review added!")
    
    def show_reviews(self):
        print("Reviews")
        for r in self._reviews:
            print(f"- {r}")

b1 = Book("It ends with us", "Dummy")
# b1.count_reviews()
# b1.add_review("good")
# b1.add_review("amazing")
# b1.add_review("just average")
# b1.add_review("mind blowing")
# b1.add_review("exciting")
# b1.add_review("very good")
# b1.add_review("found interesting")
# b1.add_review("heartbreaking")
# b1.show_reviews()
# b1.count_reviews()
# print(b1.title, b1.author)

#3----------------------------------------
class Student:
    def __init__(self, name, roll_no, marks):
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)
    
    def set_name(self, name):
        if name == "":
            print("Name cannot be empty!")
        else:
            self._name = name
            print("name updated!")
    
    def get_name(self):
        print(f"Name = {self._name}")
            
    def set_roll_no(self, roll_no):
        if (roll_no >= 1 and roll_no <= 100):
            self._roll_no = roll_no
            print("roll no updated!")
        else:
            print("Roll no should be in between 1 to 100")
            
    def get_roll_no(self):
        print(f"Roll No. = {self._roll_no}")
    
    def set_marks(self, marks):
        if marks < 0:
            print("Marks cannot be negative")
        else:
            self._marks = marks
            print("marks updated!")
            
    def get_marks(self):
        print(f"Marks = {self._marks}")

# s1 = Student("Shreya",1 ,10)
# s1.get_name()
# s1.get_roll_no()
# s1.get_marks()
        
#4----------------------------------------
class Shape:
    def area(self):
        print("Area calculation are not defined yet")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        area = 3.14 * self.radius * self.radius
        print(f"Area of circle = {area}")
        
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        area = self.length * self.width
        print(f"Area of rectangle = {area}")
        
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        area = 0.5 * self.base * self.height
        print(f"Area of triangle = {area}")

# c1 = Circle(6)
# c1.area()
# r1 = Rectangle(6, 4)
# r1.area()
# t1 = Triangle(10, 2)
# t1.area()

#5-----------------------------------
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats
        
    def get_details(self):
        print("Car Details---------")
        print(f"Brand = {self.brand}")
        print(f"Model = {self.model}")
        print(f"Seats = {self.seats}")

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc
    
    def get_details(self):
        print("Bike Details---------")
        print(f"Brand = {self.brand}")
        print(f"Model = {self.model}")
        print(f"Engine CC = {self.engine_cc}")

# c1 = Car("Hyundai", "Sedans", 6)
# c1.get_details()

# b1 = Bike("Royal enfied", "bullet", "350cc")
# b1.get_details()

#6---------------------------------
from abc import ABC, abstractmethod
class Employee:
    @abstractmethod
    def calculate_salary(self):
        pass
    
class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend
        
    def calculate_salary(self):
        return self.stipend

class ContractEmployee(Employee):
    def __init__(self, hour_rate, hour_work):
        self.hour_rate = hour_rate
        self.hour_work = hour_work
        
    def calculate_salary(self):
        return (self.hour_work * self.hour_rate)
        
class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary
    
    def calculate_salary(self):
        return self.monthly_salary

# i1 = Intern(15000)
# print(i1.calculate_salary())  
# e1 = FullTimeEmployee(50000)
# print(e1.calculate_salary()) 
# ce1 = ContractEmployee(100000, 8)
# print(ce1.calculate_salary() )

#7-------------------------------------------
class Person:
    def __init__(self, name, age = None, address= None):
        self.name = name
        self.age = age
        self.address = address
        
    def show_details(self):
        print("person details:")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Address = {self.address}")

# p1 = Person("Khushi")
# p1 = Person("Khushi", 23)
# p1 = Person("Khushi", 23, "Agra")
# p1.show_details()
    
#8----------------------------------------------
class Player:
    player_count = 0
    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1
        
    def total_players(self):
        print(f"Total players = {Player.player_count}")
        
# p1 = Player("Shubman", "High")
# p1 = Player("Abhishek", "High")
# p1 = Player("Hardik", "High")
# p1 = Player("Jasprit", "High")
# p1 = Player("Ms dhoni", "High")
# p1 = Player("Tilak", "High")
# p1 = Player("Ishan", "High")
# p1.total_players()

#9-------------------------------------
class Herbivore:
    def eat_plants(self):
        print("Eats plants")
        
class Carnivore:
    def eat_meat(self):
        print("Eats meat")
        
class Omnivore:
    def eat_both(self):
        print("Eats both plant and animals")

class Bear(Herbivore, Carnivore, Omnivore):
    def haibtat(self):
        print("Lives in mountains and forests")

b = Bear()
# b.haibtat()
# b.eat_plants()
# b.eat_meat()
# b.eat_both()