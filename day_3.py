#loops with lists
#linear search
# num = [1,2,3,6, 10]
# idx = 0
# x = 10
# for val in num:
#     if(val == x):
#         print(idx)
#     idx += 1

#TUPLES====================================
#immutable
tuple = (1,2,3,4,5,2,4)
# print(type(tuple))

#slicing in tuple
# print(tuple[:3])

#loops
sum = 0
for val in tuple:
    sum += val
# print(sum)

#tuple methods================================

# t.index(val) #returns 1st occurence index
# t.count(val) #count total occurences
tuple.index(2)
# print(tuple.index(2))
# print(tuple.count(2))

#DISTIONARY DATATYPE IN PYTHON============================
# key:value pairs
#mutable
#unordered

dict = {
    "name":"shraddha",
    "subject":["maths", 'science'],
    "cgpa":10
    
}
dict['cgpa'] =  2
# print(dict.values())
# print(dict.get("file"))
# print('end of code')

dict.update({
    "city":"delhi"
})

# print(dict)

#SETS DATATYPE IN PYTHON==================================
#collection fo unique elements
# set is mutable
# but elements in set are immutable
#no specific order of elements

# print(s)
# print(len(s))
# s.add(5)
# print(s)

#SETS METHONDS===============================
empty_set = set()
# print(type(empty_set))
# s.remove(1)
# s.clear()
# s.pop()
s = {1,2,3,4,5}
s2 = {8, 9, 4,5, 10}

# print(s.intersection(s2))




#PRACTICE QUESTIONS==================================
info = [
    ('alice', "math"),
    ('bob', "science"),
    ('alice', "science"),
    ('charlie', "math"),
    ('bob', "math"),
    ('alice', "english"),
    ('charlie', "english"),
    ]
dict ={}
for name,course in info:
    if (dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)