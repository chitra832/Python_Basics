#1 Ask the user for a string and check whether it is a palindrome or not.
str_input = input("enter a string:")
temp_str = str_input
rev_str = ""
for ch in str_input:
    rev_str = ch + rev_str
if(rev_str == temp_str):
    print(f"{str_input} is a palindrome ")
else:
    print(f"{str_input} is not palindrome ")


#2 Given a list of integers, compute the average of all numbers in the list.
num = [1, 2, 3, 4, 5]
sum = 0
for n in num:
    sum += n
avg = sum/len(num)
print(avg)

#3 Write a program that takes a list of integers and returns a new list containing only the even numbers from the original list.
num = [1, 2, 3, 4, 5, 6]
even_num = []
print(type(even_num))
for n in num:
    if(n % 2 == 0):
        even_num.append(n)
print(even_num)

#4Inputtwolistsofintegersfromtheuser.Mergethemintoonelistandsorttheresult.
list1 = list(map(int, input("enter emelent of list 1 separated by space:").split()))
list2 = list(map(int, input("enter emelent of list 2 separated by space:").split()))
list_join = list1 + list2
list_join.sort()
print("Merged and sort list:", list_join)

#5 Given a tuple of integers, create: Q4 • A tuple of all even numbers • A tuple of all odd numbers
tup = (12, 5, 4, 10, 43, 2, 13, 7, 9, 14, 33)
even_tup = tuple(num for num in tup if num % 2 == 0)
odd_tup = tuple(num for num in tup if num % 2 != 0)
print('even tuple:', even_tup)
print('odd tuple:', odd_tup)


#6 Create a dictionary to store student names and their corresponding marks. Implement a menu-driven program that allows the user to perform the following operations:
#a. Add a student and their marks
#b. Update marks for an existing student
#c. Search for a student and display their marks
#d. Display all students and their marks
students = {}

while True:
    print("\nMenu")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    print("E - Exit")
    
    choice = input("Enter your choice: ").upper()
    if(choice == "A"):
        name = input("Enter name: ")
        marks = input("enter marks:")
        students[name] = marks
        print("Student added successfully.")
    elif(choice == "B"):
        name = input("Enter student name: ")
        if name in students:
            marks = input("enter new marks:")
            students[name] = marks
            print("Student updated successfully.")
        else:
            print("Student not found.")
    elif(choice == "C"):
        name = input("Enter student name: ")
        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found.")
    elif(choice == 'D'):
        print('\n Students and Marks:')
        for name, marks in students.items():
            print(name, ':', marks)
    elif(choice == "E"):
        print("Program ended")
        break
    else:
        print("Invalid choice. Please try again.")
              

#7 Given a list of words, create a dictionary where the keys are the words and the values are the lengths of those words.
words =["apple","banana","kiwi","cherry","mango"]
word_dict = {}
for ch in words:
    word_dict[ch] = len(ch)
print(word_dict)


#8 Write a program that takes a string from the user and prints the number of spaces in the string.
str_input = input("enter a string:")
space_count = 0
for ch in str_input:
    if(ch == " "):
        space_count += 1
print(f"Spaces in the string you enter are {space_count}")

#9 Writeaprogramtocheckwhethertwolistssharenocommonelements
# share no common elements list1 =[1,2,3,4] list2 =[5,6,7,8]# share common elements list1 =[1,2,3] list2 =[3,4]
list1 = list(map(int, input("enter 1 list element separated by space:").split()))
list2 = list(map(int, input("enter 2 list element separated by space:").split()))
common_element = set(list1) & set(list2)
if common_element:
    print(f"Lists share common elements: {common_element}")
else:
    print("List not share common elements")

#10 Given a list, print all elements that appear more than once in the list.
user_list = list(map(int, input("enter 1 list element separated by space:").split()))
seen = set()
duplicate = set()
for n in user_list:
    if n in seen:
        duplicate.add(n)
    else:
        seen.add(n)
print(f"{duplicate}: these are the duplicates in list")

#11 Ask the user for a string and print:
# •Alluniquecharacters•
# Thecountofuniquecharacters
user_str = input("enter a string:")
unique_char = set(user_str)
char_len = len(unique_char)
print(f"All unique characters are: {unique_char}")
print(f"count of unique character: {char_len}")

#12 Given a list of integers, create a new list that contains only the unique elements from the original list.
user_list = list(map(int, input("enter emelent of list separated by space:").split()))
# unique_list = list(set(list))
unique_list = list(set(user_list))
print(unique_list)

#13 Write a program that takes a string from the user and prints the frequency of each character in the string.
user_str = input("enter a string:")
char_freq = {}
for ch in user_str:
    if ch in char_freq:
        char_freq[ch] += 1
    else:
        char_freq[ch] = 1
print("Character frequency:")
for ch, freq in char_freq.items():
    print(f"{ch}: {freq}")  

    


