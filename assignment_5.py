#1==============================================
cnt = 0
# with open("names.txt", 'w') as file:
#     for i in range(5):
#         user_input = input(f"Enter name {cnt +1}:")
#         file.write(user_input + "\n")
#         cnt += 1
# print(cnt)

#2=============================================
# with open("log.txt", 'a+') as file:
#     file.write("Program run successfully")
#     file.read()

# with open("log.txt", "r") as file:
#     print(file.read())

#3=============================================
# nums = [5, 10, 15, 20, 25]
# new_nums = [num for num in nums if num >15]
# print(nums)
# print(new_nums)

#4=====================================
import json

cities = {
    "Delhi": 33000000,
    "Mumbai": 21000000,
    "Bangalore": 14000000
}

with open("cities.json", "w") as file:
    json.dump(cities, file, indent=4)
    
with open("cities.json", "r") as file:
    data = json.load(file)
    print("current cities are---------")
    for city, pop in data.items():
        print(city, "-", pop)
        
new_city = input("\nEnter a new city: ")
new_population = int(input("Enter its population: "))
data[new_city] = new_population

with open("cities.json", "w") as file:
    json.dump(data, file, indent=4)
    
    print("\nCity added successfully!")

print("\nUpdated Cities and Populations:")
for city, population in data.items():
    print(f"{city}: {population}")


#5========================================
# try:
#     with open("dummy.txt", 'r') as file:
#         file.read()
# except:
#     print("File not found!")
    