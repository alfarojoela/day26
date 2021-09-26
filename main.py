numbers = [1, 2, 3]

#example of creating a list with list comprehension:
#new_list = [new_item for item in list]  #this uses keywords to help with syntax understanding
new_list = [n + 1 for n in numbers]
print(new_list)

#the below process accomplishes the same as above code.  but does not use list comprehension process
#above is far more succinct.  below resembles more of a C++ methodology
new_list_other_way = []
for n in numbers:
    n = n+1
    new_list_other_way.append(n)
print(new_list_other_way)

double_list = [(index*2) for index in range(1,5)]
print(double_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name_item.upper() for name_item in names if len(name_item) >= 5]
print(short_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [number * number for number in numbers]

#Write your code 👆 above:

print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:
#result = [new_item for item in list if test]
result = [number for number in numbers if number%2 == 0]

#Write your code 👆 above:

print(result)



# numbers1 = open(".file1.txt")
#
# numbers1_list = numbers1.readlines()

with open("file1.txt") as numbers1_file:
    numbers1 = numbers1_file.readlines()

with open("file2.txt") as numbers2_file:
    numbers2 = numbers2_file.readlines()



result = [int(num) for num in numbers1 if num in numbers2]

# print(result_in_string)
# Write your code above 👆
print("LIST OF NUMBERS IN COMMON BETWEEN file1 and file2")
print(result)


