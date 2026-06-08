# File I/O===================================================
#open
#operations  (read, write, add new data, close, delete) a file

# File operations======================================
#open, read, close
# f = open("filepath or filename", "mode to open a file")
# f = open("sample.txt", "w+") #return file object
# f.write("random text")
# print(f.read())

# f.close()

#With keyword=========================================
#close the file automatically
# with open("sample.txt", "r") as f:
#     print(f.read())
    
#deleting a file 
import os
# os.remove("sample2.txt")

#word search==============================
#search a word and print its line 
data = True
line = 1

# with open("Sample.txt", "r") as f:
#     while data:
#         data = f.readline()
#         if ("Python" in data):
           
#             print("word found", line)
#             break
#         print(data)
#         line += 1

#Exception handling=====================================
# predict possible error and handle them 
# try, except, else, finally
# try:
#     x = int(input("Enter number:"))
#     ans = 10/x
# except ZeroDivisionError:
#     print("divide by 0 is not allowed")
# except ValueError:
#     print("divide by strings is not allowed")
# else:
#     print(f"Answer = {ans}")    
# finally:
#     print("program ends!")


#List comprehension====================================

# squares = []
# for i in range(0,6):
#     if(i % 2 == 0):
#         squares.append(i*i)
#     # print(i*i)
# print(squares)
# sq = [i*i for i in range(6) if(i%2 != 0)]
# print(sq)
# nums = [-2, -4, 3, 4,5, 2, -1]
# print(nums)
# res = [0 if val < 0 else val for val in nums ]
# print(res)

#JSON module ==============================================
# javascript object notation(format)

import json

data = {
    "name":"shraddha",
    "age":23,
    "isTeacher":True
}
# json_str = '{"name":"Khushi", "isTeacher": true}'
# json_str = json.dumps(py_obj)

# py_obj = json.loads(json_str)
# print(type(json_str), json_str)
with open("data.json", 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)
    # py_obj = json.load(f)
    # print(py_obj)